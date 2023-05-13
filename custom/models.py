#demo/api/models.py 
from django.db import models

 
class Custom(models.Model):
	cusAccount =  models.CharField(max_length=100)
	create_time =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	cusEmail =  models.CharField(max_length=100)
	cusId =  models.CharField(max_length=100)
	cusName =  models.CharField(max_length=100)
	cusNames =  models.CharField(max_length=100)
	cusPwd =  models.CharField(max_length=100)
	cusSex =  models.CharField(max_length=100)
	cusTelNumber =  models.CharField(max_length=100)
	seccode =  models.CharField(max_length=100)
	class Meta:
		db_table = 'custom'
		verbose_name = "Custom"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""