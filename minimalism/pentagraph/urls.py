from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.pentagraphmain, name="pentagraphmain"),

    path("create-plan", views.create_plan, name="create_plan")
]
