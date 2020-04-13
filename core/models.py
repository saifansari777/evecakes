from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import datetime as dt
import time

# Create your models here.


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class Flavour(models.Model):
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name

class Cake(models.Model):

	unit = (
	("KG", "kilogram"),
	("Gm", "Grams")
	)

	name = models.CharField(max_length=140)
	weight = models.PositiveIntegerField(default=0)

	weight_unit = models.CharField(choices=unit,
										max_length=40)
	flavour = models.ForeignKey(Flavour,
								null=False,
								on_delete=models.DO_NOTHING)

	vegetrian = models.BooleanField(default=False,
										null=False)
	price = models.DecimalField(max_digits=9,
									decimal_places=2,
										default=0)

	discounted = models.BooleanField(default=False)

	description = models.TextField()

	image = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100)

	last_updated = models.DateTimeField(auto_now_add = True)

	slug = models.SlugField()

	def __str__(self):
		return f'{self.name} {self.weight}'


	def get_absolute_url(self):
		return reverse("core:cake-detail", kwargs={
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

	cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

	discounted_price = models.PositiveIntegerField()

	normal_price = models.PositiveIntegerField()

	item_image = models.ImageField(
			upload_to='images/%Y/%m/%d/', default='images/%Y/%m/%d/placeholder.png', max_length=100, blank=True, null=True)

	endtime = models.DateTimeField(default=dt.datetime.now()+dt.timedelta(hours=12))

	def durationofdeal(self):
		endtime = time.mktime(self.endtime.timetuple())
		return endtime*1000
		
