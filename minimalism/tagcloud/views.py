from django.shortcuts import render, redirect

from os import error
from django.shortcuts import redirect, render, get_object_or_404
from tagcloud.models import Plan


def tagcloudmain(request):
    user = request.user
    plans = Plan.objects.filter(user=user)
    plans_length = len(plans)

    return render(request, "tagcloud.html", {'plans': plans, 'plans_length': plans_length})
