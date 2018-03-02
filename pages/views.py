from django.shortcuts import render
from django.views.generic import TemplateView


class homepageview(TemplateView):
	template_name = 'home.html'
class aboutpageview(TemplateView):
	template_name = 'about.html'

class mediapageview(TemplateView):
	template_name = 'media.html'
# Create your views here.
