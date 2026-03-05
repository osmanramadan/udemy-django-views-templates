from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.list, name='blog'),
    path('<str:slug>',views.details, name='blog-details'),
    

]