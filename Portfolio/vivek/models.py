from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.TextField(null=True,blank=True)

    