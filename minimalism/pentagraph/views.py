from django.shortcuts import render, redirect

from os import error
from django.shortcuts import redirect, render, get_object_or_404
from tagcloud.models import Plan


def pentagraphmain(request):
    user = request.user
    plans = Plan.objects.filter(user=user)
    plan1 = Plan.objects.filter(user=user, status=1)
    plan2 = Plan.objects.filter(user=user, status=2)

    plan3 = Plan.objects.filter(user=user, status=3)

    plan4 = Plan.objects.filter(user=user, status=4)

    plan5 = Plan.objects.filter(user=user, status=5)

    plan1_length = len(plan1)
    plan2_length = len(plan2)

    plan3_length = len(plan3)
    plan4_length = len(plan4)
    plan5_length = len(plan5)

    return render(request, "pentagraph.html",
                  {'plans': plans,
                   'plan1_length': plan1_length,
                   'plan2_length': plan2_length,
                   'plan3_length': plan3_length,
                   'plan4_length': plan4_length,
                   'plan5_length': plan5_length,
                   })


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


def delete_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    plan.delete()
    return redirect('pentagraphmain')
