from django.shortcuts import render,redirect
from .models import *
from json import dumps
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def base(request):
    data = list(search.objects.values())
    dataJSON = dumps(data)
    return render(request, 'base.html', {'data': dataJSON})

@login_required(login_url='/login')
def index(request):
    data = list(search.objects.values())
    dataJSON = dumps(data)
    return render(request, 'index.html', {'data': dataJSON})

@login_required(login_url='/login')   
def documents(request,name,house):   
    data_docs = list(document.objects.filter(name=name,house=house).values())
    dataJSON_docs = dumps(data_docs)
    return render(request, 'documets.html', {'data_docs': dataJSON_docs,'names':name})

def logout(request):
    auth.logout(request)
    return redirect('/')   




