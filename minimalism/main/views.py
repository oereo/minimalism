from django.shortcuts import render, redirect

from os import error
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
def indexmain(request):
    return render(request, "index.html")

def indexnav(request):
    return render(request, "nav.html")