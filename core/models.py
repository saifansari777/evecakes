from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime as dt
import time
from django.utils import timezone
# Create your models here.


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)

class ItemCategory(models.Model):
	category = models.CharField(max_length=140)

	def __str__(self):
		return self.category

class DiscountPercent(models.Model):
	discount_percentage = models.DecimalField(max_digits=2, decimal_places=0)

	def __str__(self):
		return str(self.discount_percentage)+"%"

class Flavour(models.Model):
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name

class Item(models.Model):

	unit = (
	("KG", "kilogram"),
	("Gm", "Grams")
	)

	name = models.CharField(max_length=140)

	category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

	weight = models.PositiveIntegerField(default=0)

	weight_unit = models.CharField(choices=unit,
										max_length=40)
	flavour = models.ForeignKey(Flavour,
								null=False,
								on_delete=models.DO_NOTHING)

	vegetrian = models.BooleanField(default=False,
										null=False)
	price = models.DecimalField(max_digits=9,
									decimal_places=0,
										default=0)

	discounted = models.BooleanField(default=False)

	discount = models.ForeignKey(DiscountPercent, on_delete=models.CASCADE, default=0, blank=True, null=True)

	description = models.TextField()

	image = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100)

	last_updated = models.DateTimeField(auto_now_add = True)

	slug = models.SlugField()

	def __str__(self):
		return f'{self.name} {self.weight}'


	def get_absolute_url(self):
		return reverse("core:item-detail", kwargs={
			"slug": self.slug
			})

	def get_add_to_cart_url(self):
		return reverse("cart:add-to-cart", kwargs={
			"slug": self.slug
			})

	def get_remove_from_cart_url(self):
		return reverse("cart:remove-from-cart", kwargs={
			"slug": self.slug
			})

	def get_discount_price(self):
		if self.discounted:
			return int(self.price*(self.discount.discount_percentage/100))
		return 0


	def get_real_price(self):
		if self.discounted:
			real_price = self.price - self.price*(self.discount.discount_percentage/100)
			return int(real_price)
		else:
			return int(self.price)


	class Meta:
		ordering = ["last_updated",]


class BannerImage(models.Model):
	
	def clean(self):
		validate_only_one_instance(self)

	image = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100)

	image2 = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100)

	image3 = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100, blank=True, null=True)


	def __str__(self):
		return "banner_image"


class DealOfTheDay(models.Model):

	def clean(self):
		validate_only_one_instance(self)

	item = models.ForeignKey(Item, on_delete=models.CASCADE)

	discounted_price = models.PositiveIntegerField()

	normal_price = models.PositiveIntegerField()

	item_image = models.ImageField(
			upload_to='images/%Y/%m/%d/', max_length=100, blank=True, null=True)

	endtime = models.DateTimeField()


	def durationofdeal(self):
		endtime = time.mktime(self.endtime.timetuple())
		return endtime*1000
		
	def is_valid(self):
		print(timezone.now() > self.endtime)
		if timezone.now() > self.endtime:
			return False
		else:
			return True

	def is_image_uploaded(self):
		if self.item_image:
			return True
		else:
			return False