from django.shortcuts import render, get_object_or_404
from django.urls import resolve
from django.views.generic import ListView, DetailView

from .models import school

# Create your views here.
class SchoolDetailView(DetailView):
	queryset = school.objects.all()

	def get_object(self):
		object = get_object_or_404(school, url_endpoint=self.kwargs['url_endpoint'])
		return object


class SchoolInternView(ListView):
	template_name = "schools/school_listmk.html"
	def get_queryset(self):
		# qs= school.objects.filter(url_endpoint="dps").first()
		# current_url = resolve(request.path_info).url_name
		# print(current_url)
		school_name=self.kwargs['url_endpoint']
		qs= school.objects.filter(url_endpoint=school_name).first()
		print(school_name)
		queryset = qs.latest_school.all()
		return queryset

class SchoolListView(ListView):
    paginate_by=2

    def get_queryset(self):
        if len(self.kwargs) > 0:
            return school.objects.filter(full_name__icontains=self.kwargs['query'])
        else:
            return school.objects.all()
