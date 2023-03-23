from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class adventureplaces(models.Model):
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="Windsor")
    country = models.CharField(max_length=50, default="Canada")
    picture=models.ImageField(upload_to='uploads/',default='/Users/harika/PycharmProjects/pythonProject/djangoProject/Hotairballonbooking/app/static/uploads/Default.jpeg')
    Description=models.TextField(max_length=2000)
    def __str__(self):
        return self.location


class bookings(models.Model):
    location = models.ForeignKey(adventureplaces, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    VIEW_CHOICES = [
        ('Day view', 'Day view'),
        ('Night view', 'Night view'),
         ]
    view = models.CharField(max_length=10, choices=VIEW_CHOICES)
    no_of_persons = models.IntegerField()
    booking_for_the_date=models.DateField(null=True)

    def __str__(self):
        return self.view




