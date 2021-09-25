from django.urls import path
from . import views


urlpatterns = [
    path('test_page/', views.test_page, name="test_page"),
    path('result_page1/', views.result_page1, name="result_page1"),
    path('result_page2/', views.result_page2, name="result_page2"),
    path('result_page3/', views.result_page3, name="result_page3"),
    path('result_page4/', views.result_page4, name="result_page4"),
    path('result_page5/', views.result_page5, name="result_page5"),
]
