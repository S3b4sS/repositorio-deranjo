from django.shortcuts import render
#generic views for work with templates 
from django.views.generic import TemplateView

# Create your views here idiot.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"