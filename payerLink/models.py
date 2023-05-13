
from django.db import models

 
class PayerLink(models.Model):
	link =  models.CharField(max_length=100)
	name =  models.CharField(max_length=100)
	username =  models.CharField(max_length=100)
	class Meta:
		db_table = 'payer_link'
		verbose_name = "PayerLink"
		verbose_name_plural = verbose_name
	def __str__(self):  
		return ""