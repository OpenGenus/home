from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView

from pages.models import intern
from schools.models import school
# Create your views here.

def internDetailView(request,username):
	return HttpResponse("Hi")
# class InternDetailView(DetailView):
# 	return HttpResponse("Hi")

class InternListView(ListView):
	queryset=intern.objects.all()
	paginate_by=2

class InternDetailView(DetailView):
	queryset = intern.objects.all()
	slug_field = 'username'