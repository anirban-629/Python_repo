from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()

# for changing names in sqlite
    def __str__(self) :
        return self.name