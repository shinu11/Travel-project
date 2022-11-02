from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default='false')


class blog(models.Model):
    date=models.DateField('datepublished')
    image=models.ImageField(upload_to='photo')
    title=models.CharField(max_length=100)
    subhead=models.TextField()
    desc=models.TextField()


