from django.shortcuts import render, redirect 
from .models import * 
from .form import *


# Create your views here.
def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'forum_app/home.html',context)

def addinforum(request):
    form = Createinforum()
    if request.method == 'POST':
        form = Createinforum(request.POST, request.FILES)   
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'forum_app/addinforum.html',context)     

def addindiscussion(request):
    form = Createindiscussion()
    if request.method == 'POST':
        form = Createindiscussion(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'forum_app/addindiscussion.html',context) 

