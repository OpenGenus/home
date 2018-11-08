from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import school
# Create your views here.
class SchoolDetailView(DetailView):
	queryset = school.objects.all()

	def get_object(self):
		object = get_object_or_404(school, url_endpoint=self.kwargs['url_endpoint'])
		return object
	

class SchoolInternView(ListView):
	queryset= school.objects.all()
