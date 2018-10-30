from django.db import models


POSITION_CHOICES=(
	('Intern','INTERN'),
	('Software developer','SOFTWARE DEVELOPER'),
	('Founder','FOUNDER'),
	)
# Create your models here.
class Interns(models.Model):
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

	def __str__(self):
		return self.name

