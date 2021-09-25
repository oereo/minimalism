from django.urls import path
from . import views

urlpatterns = [
    path("",views.indexmain,name="indexmain"),
    path("nav/",views.indexnav,name="indexnav"),
]