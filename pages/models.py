from django.db import models


POSITION_CHOICES=(
	('intern','INTERN'),
	('software developer','SOFTWARE DEVELOPER'),
	('founder','FOUNDER'),
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
	picture_upload	=	models.FileField(null=True,blank=True)
	work_done		=	models.CharField(max_length=120)

	def __str__(self):
		return self.name

