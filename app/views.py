from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *


def insert_topic(request):
        if request.method=='POST':
            tn=request.POST['tn']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            QLTO=Topic.objects.all()
            d={'topic':QLTO}
            return render(request,'display_topic.html',d)

        return render(request,'insert_topic.html')


def insert_webpage(request):
      QLTO=Topic.objects.all()
      d={'topic':QLTO}
      if request.method=='POST':
            tn=request.POST['tn']
            nm=request.POST['nm']
            ur=request.POST['ur']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=ur)[0]
            WO.save()

            QLWO=Webpage.objects.all()

            d1={'webpage':QLWO}
            
            return render(request,'display_webpage.html',d1)
      return render(request,'insert_webpage.html',d)
        