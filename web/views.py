from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import HttpResponse

from posts.models import Event, Customer


def index(request):
    events = Event.objects.filter(is_deleted=False,single_time=True)
    customers = Customer.objects.all()
    print(datetime.now().date())

    sortby = request.GET.get('sort', '')
    print(sortby)
    today = datetime.now().date()
    month = datetime.now().month

    if sortby == "today":
        events = Event.objects.filter(event_date=today)
        print('today events only')
    elif sortby == "month":
        events = Event.objects.filter(event_date__month=month)
    elif sortby == "week":
        dt = datetime.strptime(today.strftime("%Y%m%d"), '%Y%m%d')
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)

        events = Event.objects.filter(event_date__range=[start, end])

    search_customers = request.GET.getlist("user")
    print(search_customers)

    if search_customers:
        events = events.filter(user__in=search_customers)

    context = {
        "title": "Home Page",
        "events": events,
        "customers": customers,

    }
    return render(request, 'web/index.html', context=context)
