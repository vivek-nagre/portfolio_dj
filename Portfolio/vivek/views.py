from django.shortcuts import render
from django.http import HttpResponse
import datetime,random
from vivek.models import Contact
# Create your views here.
def index(request):
    count=random.randint(1000,5000)
    time = datetime.datetime.now()
    con={'time':time,"count":count}
    return render(request,'vivek/home.html',con)
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        print(name," ",email)
        contact=Contact()
        contact.name=name
        contact.email=email
        contact.phone=phone
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1>thank you </h1>")

         

    return render(request,'vivek/contact.html')