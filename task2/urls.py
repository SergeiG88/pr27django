from django.urls import path
from . import views

urlpatterns = [
    path('class/', views.class_view, name='class_view'),
    path('function/', views.function_view, name='function_view'),
]