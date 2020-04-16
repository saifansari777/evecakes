from django.db import models
from django.conf import settings
from core.models import Item
# Create your models here.


class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	ordered = models.BooleanField(default=False)

	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.quantity} of {self.item.name}'

	def get_total_price(self):
		print(self.quantity * self.item.get_real_price())
		return self.quantity * self.item.get_real_price()

	def get_total_discount_price(self):
		return self.quantity * self.item.get_discount_price()
 
class Order(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
		
	ordered = models.BooleanField(default=False)

	items = models.ManyToManyField(OrderItem)

	start_date = models.DateTimeField(auto_now_add=True)

	ordered_date = models.DateTimeField()

	def __str__(self):
		return self.user.username+"'s Order"

	def get_final_price(self):
		total = 0
		for item in self.items.all():
			total += item.get_total_price()
		return total