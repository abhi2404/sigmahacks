from django.db import models
from registration.models import user, shopkeeper


# Create your models here.
class shoppinglist(models.Model):
    date=models.TimeField(auto_now_add=False,blank=True)
    Status=models.CharField(max_length=20,default="pending")
    key=models.ForeignKey('registration.user',models.DO_NOTHING,null=True)
    link=models.ForeignKey('registration.shopkeeper',models.DO_NOTHING,null=True)


class timeforcust(models.Model):
	key=models.ForeignKey('registration.user',models.DO_NOTHING,null=True)
	link = models.ForeignKey('registration.shopkeeper',models.DO_NOTHING,null=True)
	timing = models.TimeField( auto_now_add=False)
	people_count = models.IntegerField()    