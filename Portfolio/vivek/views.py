from django.shortcuts import render
import datetime,random
# Create your views here.
def index(request):
    
    count=random.randint(1000,5000)
    time = datetime.datetime.now()
    con={'time':time,"count":count}
    return render(request,'vivek/home.html',con)