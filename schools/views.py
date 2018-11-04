from django.shortcuts import render
from django.views.generic import DetailView

from .models import school
# Create your views here.
class SchoolDetailView(DetailView):
	queryset = school.objects.all()