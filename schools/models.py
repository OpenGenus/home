from django.db import models
from django.db.models.signals import pre_save

from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models


from .utils import unique_slug_generator


# Create your models here.
class school(models.Model):
	full_name			=	models.CharField(max_length=120, unique=True)
	short_name			=	models.CharField(max_length=120, unique=True)
	url_endpoint		=	models.SlugField(null=True,blank=True)
	# description			=	models.TextField(max_length=1000)
	location			=	models.CharField(max_length=30)
	official_link		=	models.URLField(max_length=120,unique=True)
	logo_picture		=	models.ImageField(null=True,blank=True,
											height_field="height_field",
											width_field="width_field")
	height_field		=	models.IntegerField(default=0)
	width_field			=	models.IntegerField(default=0)
	established_date	=	models.DateField()
	description			=	HTMLField(null=True,blank=True)
	opengenus_rating    =   models.FloatField(default=0)


	def __str__(self):
		return self.full_name

	def get_rating_perc(self):
		return int((self.opengenus_rating/5)*100)

	class Meta:
		ordering = ["-established_date"]

def school_pre_save_receiver(sender, instance, *args,**kwargs):
	if not instance.url_endpoint:
		instance.url_endpoint = unique_slug_generator(instance)


pre_save.connect(school_pre_save_receiver, sender=school)
