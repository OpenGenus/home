from django.db import models
from django.urls import reverse
from schools.models import school

POSITION_CHOICES=(
	('Intern','INTERN'),
	('Software developer','SOFTWARE DEVELOPER'),
	('Founder','FOUNDER'),
	)
# Create your models here.
class intern(models.Model):
	username		=	models.CharField(max_length=120,unique=True)
	name			=	models.CharField(max_length=120) 
	discourse_url	=	models.URLField(max_length=120,unique=True)
	location		=	models.CharField(max_length=120)
	introduction	=	models.TextField(max_length=1000)
	position		=	models.CharField(max_length=30, choices=POSITION_CHOICES,default='Intern')
	start_date		= 	models.DateField(max_length=120)
	finish_date		= 	models.DateField(max_length=120)
	picture_upload	=	models.ImageField(null=True,blank=True,
											height_field="height_field",
											width_field="width_field")
	work_done		=	models.CharField(max_length=120)
	fav_experience	=	models.TextField(max_length=1000,null=True,blank=True)
	height_field	=	models.IntegerField(default=0)
	width_field		=	models.IntegerField(default=0)
	latest_school	=	models.ForeignKey(school, on_delete = models.CASCADE, related_name='latest_school', default=1)
	prev_school_1	=	models.ForeignKey(school, on_delete = models.CASCADE, 
										null=True, blank=True,related_name='prev_school_1')
	prev_school_2	=	models.ForeignKey(school, on_delete = models.CASCADE,
										null=True, blank=True, related_name='prev_school_2')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-finish_date"]

	def get_absolute_url(self):
		return reverse('intern-detail',args=[str(self.username)])

	def save(self, *args, **kwargs):
		self.username = self.username.lower()
		super().save(*args, **kwargs)

# class Schools(models.Model):
# 	full name			=	models.CharField(max_length=120, unique=True) 
# 	short name			=	models.CharField(max_length=30, unique=True)
# 	url_id				=	models.URLField(max_length=120, unique=True)
# 	description			=	models.TextField(max_length=500)
# 	location			=	models.CharField(max_length=120)
# 	official_link		=	models.URLField(max_length=120, unique=True)
# 	logo_picture		=	models.
# 	established_date