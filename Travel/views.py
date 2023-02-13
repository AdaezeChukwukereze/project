from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Travel.models import Locate

class Home(ListView):
    model = Locate
    template_name='Travel/index.html'
    context_object_name='locate'

class Detail(DetailView):
    model= Locate
    template_name= 'Travel/index.html'
    context_object_name='locate'
