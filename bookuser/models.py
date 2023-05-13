#demo/api/models.py 
from django.db import models

 
class BookUser(models.Model):
	cusAccount =  models.CharField(max_length=100)
	create_time =  models.CharField(max_length=100)
	status =  models.CharField(max_length=100)
	reserve1 =  models.CharField(max_length=100)
	reserve2 =  models.CharField(max_length=100)
	reserve3 =  models.CharField(max_length=100)
	reserve4 =  models.CharField(max_length=100)
	reserve5 =  models.CharField(max_length=100)
	cusId =  models.CharField(max_length=100)
	booBerth =  models.CharField(max_length=100)
	comCode =  models.CharField(max_length=100)
	cusTelNumber =  models.CharField(max_length=100)
	fliYfare =  models.CharField(max_length=100)
	class Meta:
		db_table = 'book_user'
		verbose_name = "BookUser"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""