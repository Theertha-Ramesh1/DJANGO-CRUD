from django.shortcuts import render, redirect
from App3.forms import *
from App3.models import *


def insert(request):
    print("mm")
    if request.method == "POST":
        print("nn")
        form = Loginform(request.POST)
        print("kk")
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/')
            except:
                pass


    else:
        form = Loginform()
    return render(request, "index.html", {"form": form})

# "form" is using in index page for value getting

def show(request):
    form = Login.objects.all()
    return render(request,'show.html',{'form': form})


def edit(request,id):
    emp = Login.objects.get(id= id)
    print("kkkk")
    return render(request,'edit.html',{'emp': emp})


def update(request,id):
    emp = Login.objects.get(id=id)
    log = Loginform(request.POST,instance= emp)        # instance is using for update the existing row otherwise create a new field

    if log.is_valid():
        log.save()
        return redirect("/show/")

    return render(request,'edit.html',{"emp": emp})


def delete(request,id):
    form = Login.objects.get(id= id)
    form.delete()
    return redirect("/show/")
