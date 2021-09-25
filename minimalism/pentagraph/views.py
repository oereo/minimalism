from django.shortcuts import render, redirect

from os import error
from django.shortcuts import redirect, render, get_object_or_404
from tagcloud.models import Plan


def pentagraphmain(request):
    user = request.user
    plans = Plan.objects.filter(user=user)

    return render(request, "pentagraph.html", {'plans': plans})


def create_plan(request):
    user = request.user
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        status = request.POST['drop1']
        Plan.objects.create(
            title=title,
            content=content,
            clean_date=date,
            status=status,
            user=user
        )
        return redirect('pentagraphmain')
    return redirect('pentagraphmain')
