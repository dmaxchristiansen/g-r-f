from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from apps.social_app.models import Project
import bcrypt

def home(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, "log_reg_app/home.html", context)

def about(request):
    return render(request, "log_reg_app/about.html")

def registration(request):
    return render(request, "log_reg_app/registration.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/registration")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)
        first_name = request.POST['first_name']
        if 'prof_pic' in request.FILES:
            prof_pic = request.FILES['prof_pic']
            fs = FileSystemStorage()
            filename = fs.save(first_name, prof_pic)
            uploaded_prof_pic_url = fs.url(filename)
            user = User.objects.create(first_name=first_name, last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash, level=request.POST['level'], prof_pic=prof_pic, url=uploaded_prof_pic_url)
        else:
            user = User.objects.create(first_name=first_name, last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash, level=request.POST['level'])
        if user:
            request.session['userid']=user.id
            return redirect("/registered")

def registered(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, "log_reg_app/registered.html", context)

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid']=logged_user.id
            return redirect("/success")
    return redirect("/")

def success(request):
    if 'userid' not in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session['userid'])
    context = {
        "user": user,
    }
    return render(request, "log_reg_app/success.html", context)


def logout(request):
    if 'userid' not in request.session:
        return redirect("/")
    else:
        del request.session['userid']
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, "log_reg_app/logged_out.html", context)