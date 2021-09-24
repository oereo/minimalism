from django.shortcuts import render, redirect

from os import error
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.
def main(request):
    return render(request, "tagcloud.html")
