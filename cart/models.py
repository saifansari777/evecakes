from django.db import models
from django.conf import settings
from core.models import Cake
# Create your models here.
class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	ordered = models.BooleanField(default=False)

	item = models.ForeignKey(Cake, on_delete=models.CASCADE)
	
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return self.item.name


class Order(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		
	ordered = models.BooleanField(default=False)

	items = models.ManyToManyField(OrderItem)

	start_date = models.DateTimeField(auto_now_add=True)

	ordered_date = models.DateTimeField()

	def __str__(self):
		return self.user.username