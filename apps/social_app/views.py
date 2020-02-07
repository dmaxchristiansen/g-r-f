from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from apps.log_reg_app.models import User
from .models import Project, Message
from decimal import *


def profile(request, number):
    if 'userid' not in request.session:
        return redirect("/")
    print(request.session['userid'])
    if number == request.session['userid']:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "user_in_profile": User.objects.get(id=request.session['userid']),
        }
    else:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "user_in_profile": User.objects.get(id=number)
        }
    return render(request, "social_app/profile.html", context)

def updateProfPic(request):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    new_prof_pic = request.FILES['prof_pic']
    fs = FileSystemStorage()
    filename = fs.save(user.first_name, new_prof_pic)
    uploaded_new_prof_pic_url = fs.url(filename)
    user.prof_pic = request.FILES['prof_pic']
    user.save()
    user.url = uploaded_new_prof_pic_url
    user.save()
    num=request.session['userid']
    return redirect(f'/profile/{num}')
    
    

def newProject(request):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    context = {
        "user": user,
    }
    return render(request, "social_app/new_project.html", context)

def createNewProject(request):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    name = request.POST['name'] 
    proj_pic = request.FILES['proj_pic']
    fs = FileSystemStorage()
    filename = fs.save(name, proj_pic)
    uploaded_proj_pic_url = fs.url(filename)
    Project.objects.create(user=user, proj_type=request.POST['proj_type'], name=name, location=request.POST['location'], desc=request.POST['desc'], proj_pic=proj_pic, url=uploaded_proj_pic_url)
    print(request.FILES['proj_pic'])
    return redirect('/projects')

def projects(request):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    context = {
        'projects': Project.objects.all().order_by("created_at"),
        "user": user,
    }
    return render(request, "social_app/projects.html", context)

def project(request, number):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    context = {
        'project': Project.objects.get(id=number),
        "user": user,
    }
    return render(request, "social_app/project.html", context)

def postMessage(request, number):
    if 'userid' not in request.session:
        return redirect("/")
    message = Message.objects.create(message=request.POST["message"], project=Project.objects.get(id=number), user=User.objects.get(id=request.session['userid']))
    print(message.message)
    return redirect(f"/project/{number}")

def donate(request, number):
    if 'userid' not in request.session:
        return redirect("/")
    donation = request.POST['donation']
    dec_donation = Decimal(donation)
    print(dec_donation)
    project = Project.objects.get(id=number)
    project.funds += dec_donation
    project.save()
    return redirect(f"/project/{number}")