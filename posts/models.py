import uuid

from django.db import models


class Event(models.Model):
    CHOICES = (
        ('MARRIAGE' , 'marriage'),
        ('BIRTHDAY' , 'birthday'),
        ('FUNERAL' , 'funeral'),
        ('ENGAGEMENT','engagement'),
        ('BAPTISM', 'baptism'),
        ('HOUSE WARMING','house warming')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='events/')
    event_type = models.CharField(max_length=255 ,choices=CHOICES)
    event_date = models.DateField(max_length=64)
    single_time = models.BooleanField(default=True)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.first_name
