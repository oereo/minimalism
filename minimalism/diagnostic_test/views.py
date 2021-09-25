from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.template import loader

# Create your views here.

# test_page
def test_page(request):
    return render(request,"diagnostic_test/test_page.html")

def result_test(request):
    if request.method=="POST":
        check = int(request.POST['nameOfchecked'])
        if(check>=18):
            return render(request,"diagnostic_test/result_page1.html")
        elif(check>=13):
            return render(request,"diagnostic_test/result_page2.html")
        elif(check>=7):
            return render(request,"diagnostic_test/result_page3.html")
        elif(check>=3):
            return render(request,"diagnostic_test/result_page4.html")
        else:
            return render(request,"diagnostic_test/result_page5.html")



# result_page
def result_page1(request):
    return render(request, "diagnostic_test/result_page1.html")

def result_page2(request):
    return render(request, "diagnostic_test/result_page2.html")

def result_page3(request):
    return render(request, "diagnostic_test/result_page3.html")

def result_page4(request):
    return render(request, "diagnostic_test/result_page4.html")    

def result_page5(request):
    return render(request, "diagnostic_test/result_page5.html") 
