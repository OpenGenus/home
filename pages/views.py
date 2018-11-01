from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView

from pages.models import Interns
# Create your views here.

def internDetailView(request,username):
	return HttpResponse("Hi")
# class InternDetailView(DetailView):
# 	return HttpResponse("Hi")

class InternListView(ListView):
	queryset=Interns.objects.all()
	paginate_by=2

class InternDetailView(DetailView):
	queryset = Interns.objects.all()
	slug_field = 'username'