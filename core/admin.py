from django.contrib import admin
from .models import Cake, Flavour, BannerImage
# Register your models here.
admin.site.register(Cake)
admin.site.register(Flavour)
admin.site.register(BannerImage)