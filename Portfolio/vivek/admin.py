from django.contrib import admin
from vivek.models import Contact
# Register your models here.
class Admincontact(admin.ModelAdmin):
    list_display=['id','name','email','subject']
admin.site.register(Contact,Admincontact)