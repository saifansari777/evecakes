from django.db import models
from django.core.exceptions import ValidationError
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
	("G", "Grams")
	)

	name = models.CharField(max_length=140)
	weight = models.DecimalField(max_digits=9,
											decimal_places=2,default=0)

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
			upload_to='images/', default='images/placeholder.png', max_length=100)

	last_updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f'{self.name} {self.weight}'

class BannerImage(models.Model):
	
	def clean(self):
		validate_only_one_instance(self)

	image = models.ImageField(
			upload_to='images/', default='images/placeholder.png', max_length=100)

	image2 = models.ImageField(
			upload_to='images/', default='images/placeholder.png', max_length=100)

	image3 = models.ImageField(
			upload_to='images/', default='images/placeholder.png', max_length=100, blank=True, null=True)


	def __str__(self):
		return "banner_image"


# class ShoppingCartItem(models.Model):
#     quantity = models.IntegerField(null=False)

#     price_per_unit = models.DecimalField(max_digits=9,decimal_places=2,default=0)

#     cart = models.ForeignKey(ShoppingCart,
#                              null=False,
#                              on_delete=models.CASCADE)
#     cake = models.ForeignKey(Cake,
#                              null=False,
#                              on_delete=models.CASCADE)
