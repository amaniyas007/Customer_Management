import json

from django.shortcuts import render,get_object_or_404,render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from posts.forms import EventForm
from posts.models import Event
from main.functions import generate_form_errors


@login_required(login_url='/users/login/')
def create_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            print(form.cleaned_data)
            form.save()
            
            
            response_data = {
                "status": "success",
                "title": "Success",
                "message": "Submitted successfully",
                "redirect": 'true',
                "redirect_url": reverse('web:index')
            }

            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        
        print(generate_form_errors(form))
        response_data = {
            "status": "false",
            "title": "Failed",
            "message": generate_form_errors(form),
        }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    else:

        form = EventForm()
        context = {
            "title": "Add New Events",
            "form": form
        }
        return render(request, "posts/create.html", context=context)


@login_required(login_url='/users/login/')
def detail_event(request, pk):
    return render(request)


@login_required(login_url='/users/login/')
def edit_event(request, pk):
    instance = Event.objects.get(pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            response_data = {
                "status": "success",
                "title": "Successfully Updated",
                "message": "Event Updated Successfully.",
                "redirect": 'true',
                "redirect_url": reverse('web:index')
            }
        else:
            message = generate_form_errors(form)
            response_data = {
                "status": "false",
                "title": "Failed",
                "message": message
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    form = EventForm(instance=instance)

    context = {
        "title": "Edit Event",
        'form': form,
        'instance':instance,
    }
    return render(request, 'posts/edit.html', context)


@login_required(login_url='/users/login/')
def delete_event(request, pk):
    Event.objects.filter(pk=pk).update(
        is_deleted=True,
    )
    return HttpResponseRedirect(reverse('web:index'))