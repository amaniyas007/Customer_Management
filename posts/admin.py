from django.contrib import admin
from posts.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name',  'email']


admin.site.register(Customer, CustomerAdmin)
