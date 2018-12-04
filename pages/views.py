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
	paginate_by=2
	def get_queryset(self):
		if len(self.kwargs) > 0:
			return intern.objects.filter(name__icontains=self.kwargs['query'])
		else:
			return intern.objects.all()

class InternDetailView(DetailView):
	queryset = intern.objects.all()
	slug_field = 'username'
