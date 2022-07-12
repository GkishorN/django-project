from django.db import models

# Create your models here.


class Customer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	Subject1_mark = models.CharField(max_length=200)
	Subject2_mark = models.CharField(max_length=200)
	Subject3_mark = models.CharField(max_length=200)
	Subject4_mark = models.CharField(max_length=200)



	def __str__(self):
		return self.first_name + ' ' + self.last_name 
		return self.Subject1_mark
		return self.Subject2_mark
		return self.Subject3_mark
		return self.Subject4_mark 
