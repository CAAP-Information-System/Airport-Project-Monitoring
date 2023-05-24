from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views import generic 
from django.contrib import messages
from django.db.models import Q
import datetime

  
# Create your views here.
from .models import Bulletin, BulletinFile, Aknowledge, BulletinComment
from .forms import PostForm






