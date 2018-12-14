from django.contrib.sitemaps import Sitemap
from schools.models import school
from pages.models import intern
from django.urls import reverse

class SchoolSitemap(Sitemap):

	def items(self):
		return school.objects.all()

class InternSitemap(Sitemap):

	def items(self):
		return intern.objects.all()

class StaticViewSitemap(Sitemap):

	def items(self):
		return ['index','cosmos','quark','search','iq','discuss']

	def location(self, item):
		return reverse(item)