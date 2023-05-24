from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
from django.contrib import messages
from django.db.models import Q
from django.views.static import serve
from datetime import datetime, timezone, date

from .models import AiportProject
from .forms import AiportProjectForm
from django.views.decorators.clickjacking import xframe_options_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'dashboard/projects/login.html', {'error_message': error_message})

@login_required

def logout_view(request):
    logout(request)
    return redirect('auth')

def addnew(request):
    context = {}
 
    # add the dictionary during initialization
    form = AiportProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "dashboard/projects/add_record.html", context)


def index(request):
    projects = AiportProject.objects.all()  
    count_all = AiportProject.objects.all().count() 
    count_complete = AiportProject.objects.filter(status="Complete").count()
    count_ongoing = AiportProject.objects.filter(status="On-Going").count()
    count_procurement = AiportProject.objects.filter(status="Under Procurement").count()

    return render(request,"dashboard/projects/project_table.html",{'projects':projects, 'count_all':count_all, 'count_complete':count_complete, 'count_ongoing':count_ongoing, 'count_procurement':count_procurement})  


def edit(request, id):  
    project = AiportProject.objects.get(id=id)  

    return render(request,'dashboard/projects/edit.html', {'project':project})  

def show_project(request, id): 
    context ={}

    context["project"] = AiportProject.objects.get(id = id)
          
    return render(request, "dashboard/projects/show_project.html", context)

def update(request, id):  

    return HttpResponse(request)  


def destroy(request, id):  
    AiportProject = AiportProject.objects.get(id=id)  
    AiportProject.delete()  
    return redirect("/") 


def infoView(request):
    return render(request,'dashboard/projects/info.html')

def viewProject(request,id):

    view_proj = AiportProject.objects.get(id = id)

    
        # green
    if view_proj.progress >= 90 and view_proj.progress <= 100:
        progress_color = "#5FD068"
        # blue
    if  view_proj.progress >= 75 and view_proj.progress <= 89:        
        progress_color = "#62CDFF"
        # yello
    if  view_proj.progress >= 30 and view_proj.progress <= 74:
        progress_color = "#FFE15D"
        # red
    if  view_proj.progress >= 0 and view_proj.progress <= 29:
        progress_color = "#FD8A8A"
    
    return render(request,'dashboard/projects/view.html', {'progress_color': progress_color, 'view' : view_proj })

def showView(request,id):
    context = {}
    context["proj_detail"] = AiportProject.objects.get(id=id)
    return render(request,'dashboard/projects/show.html')


def dashView(request):
    projects = AiportProject.objects.all()[:300] 
    count_all = AiportProject.objects.all().count()
    count_complete = AiportProject.objects.filter(status="Completed").count()
    count_ongoing = AiportProject.objects.filter(status="On- going").count()
    count_procurement = AiportProject.objects.filter(status="under procurement").count()
    return render(request,"dashboard/projects/dashboard.html",{'projects':projects, 'count_all':count_all, 'count_complete':count_complete, 'count_ongoing':count_ongoing, 'count_procurement':count_procurement})

def complete_projects(request):
    complete = AiportProject.objects.filter(status='Complete').all()

    return render(request,'dashboard/projects/complete_dashboard/projects/html', {'complete': complete})


def Project(request, name):    
    projects = AiportProject.objects.filter(location__icontains= name).order_by('-id').all()

    return render(request,'dashboard/projects/projects.html', {'projects': projects})

def ongoing_projects(request):
    ongoing = AiportProject.objects.filter(status='On-Going').all()

    return render(request,'dashboard/projects/ongoing_dashboard/projects/html', {'ongoing': ongoing})


def procurement_projects(request):
    procurement = AiportProject.objects.filter(status='Under Procurement').all()

    return render(request,'dashboard/projects/procurement_dashboard/projects/html', {'procurement': procurement})

def progress_view(request):
    # Calculate the progress as a percentage of the target number of signups
    total_capacity = 100  # Replace with your own target number
    users = 31
    comp_projects = AiportProject.objects.filter(status='Complete').count()
    ongoing_projects = AiportProject.objects.filter(status='On-Going').count()
    proc_projects = AiportProject.objects.filter(status='Under Procurement').count()
    progress_cp = comp_projects / total_capacity * 100 
    # * 100 is a conversion of int to float
    progress_og = ongoing_projects / total_capacity * 100
    progress_proc = proc_projects / total_capacity * 100
    high = 'green'
    medium = 'orange'
    low = 'red'
    if progress_cp < 30:
        progress_color = low
    elif progress_cp < 80:
        progress_color = medium

    else:
        progress_color = high

    # Render a template that displays the progress bar
    context = {
        'progress_color': progress_color,
        'progress_cp':progress_cp,
        'progress_og':progress_og,
        'progress_proc':progress_proc,
    }

    return render(request, 'dashboard/projects/sample.html', context)





