import imp
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def Index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title != "":
            ToDo.objects.create(title=title)
        return redirect('index')

    data = ToDo.objects.all
    data_dict = {"data": data}

    return render(request, 'index.html', context=data_dict)

def Delete(request, id =  None):
    ToDo.objects.get(id=id).delete()

    return redirect('index')

def Complete(request, id = None):
    data = ToDo.objects.get(id=id)
    data.complete = True
    data.save()

    return redirect('index')

def InComplete(request, id = None):
    data = ToDo.objects.get(id=id)
    data.complete = False
    data.save()

    return redirect('index')