from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting



def welcome(request):
    return render(request,"website/welcome.html",{"meetings":Meeting.objects.all()})
# Create your views here.
def about(request):
    return HttpResponse("I'am Tanjiro <br> From Demon Slayer Core")  