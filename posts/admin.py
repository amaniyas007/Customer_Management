from django.contrib import admin
from posts.models import Customer, Event


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['address',  'email']


admin.site.register(Customer, CustomerAdmin)

admin.site.register(Event)