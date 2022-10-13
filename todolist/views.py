from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from django.contrib import messages
from todolist.models import Task
from django.urls import reverse
from django.core import serializers
import datetime

# Create your views here.

@login_required(login_url="/todolist/login/")
def show_todolist(request):
    todolist_objects = Task.objects.filter(user=request.user)
    context = {
        "todolist": todolist_objects, 
        "username": request.user.username
        }
    return render(request, "todolist.html", context)

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("todolist:login")
    
    return render(request, "register.html", {"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie("last_login", str(datetime.datetime.now()))  
            return response
        else:
            messages.info(request, "Username or Password is incorrect!")

    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("todolist:login"))
    response.delete_cookie("last_login")
    return response


@login_required(login_url="/todolist/login/")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))

    return render(request, "create_task.html")

@login_required(login_url="/todolist/login/")
def delete_task(request, id):
    task = Task.objects.get(user = request.user, pk = id)
    task.delete()

    return redirect(
        "todolist:show_todolist"
    )

@login_required(login_url="/todolist/login/")
def delete_task_with_ajax(request, id):
    if request.method == "DELETE":
        task = Task.objects.get(user=request.user, id=id)
        task.delete()

        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()

@login_required(login_url="/todolist/login/")
def update_task(request, id):
    task = Task.objects.get(user = request.user, pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect("todolist:show_todolist")

@login_required(login_url="/todolist/login/")
def show_json(request):
    task = Task.objects.all()
    return HttpResponse(serializers.serialize("json", task))

@login_required(login_url="/todolist/login/")
def add_task_with_ajax(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task(
            user=request.user,
            title=title,
            description=description,
            date=datetime.datetime.today(),
            is_finished = False
        )
        task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()