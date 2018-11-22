from django.contrib.sitemaps import Sitemap
from schools.models import school
from pages.models import intern

class SchoolSitemap(Sitemap):

	def items(self):
		return school.objects.all()

class InternSitemap(Sitemap):

	def items(self):
		return intern.objects.all()
