from django.db import models

# Create your models here.
class school(models.Model):
	full_name			=	models.CharField(max_length=120, unique=True) 
	short_name			=	models.CharField(max_length=120, unique=True)
	url_id				=	models.URLField(max_length=120)
	description			=	models.TextField(max_length=1000)
	location			=	models.CharField(max_length=30)
	official_link		=	models.URLField(max_length=120,unique=True)
	logo_picture		=	models.ImageField(null=True,blank=True,
											height_field="height_field",
											width_field="width_field")
	height_field		=	models.IntegerField(default=0)
	width_field			=	models.IntegerField(default=0)
	established_date	=	models.DateField()

	def __str__(self):
		return self.full_name

	class Meta:
		ordering = ["-established_date"]