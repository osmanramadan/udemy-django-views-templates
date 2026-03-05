from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.template.loader import get_template



def home(request):
    
    return render(request, 'home.html', context={'my_list': [1, 2, 3, 4, 5]})