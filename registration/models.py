from django.db import models

# Create your models here.
#models to store details of user or customer 

class user(models.Model):
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=12)
	mobile_no=models.CharField(max_length=12)
	address=models.CharField(max_length=400,null=True)
	latitude=models.CharField(max_length=30,null=True)
	longitude=models.CharField(max_length=30,null=True)

#models to store deatils of shopkeeper
class shopkeeper(models.Model):
	shopname=models.CharField(max_length=30 , default="customer",null= True)
	name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=12)
	mobile_no=models.CharField(max_length=12)
	category=models.CharField(max_length=30 ,null= True)
	address=models.CharField(max_length=400,null=True)
	opentime=models.CharField(max_length=30,null=True )
	closetime=models.CharField(max_length=30,null=True )
	latitude=models.CharField(max_length=30,null=True)
	longitude=models.CharField(max_length=30,null=True)
