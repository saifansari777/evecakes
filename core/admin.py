from django.contrib import admin
from .models import Item, Flavour, BannerImage, DealOfTheDay, DiscountPercent, ItemCategory
# Register your models here.
admin.site.register(Item)
admin.site.register(Flavour)
admin.site.register(BannerImage)
admin.site.register(DealOfTheDay)
admin.site.register(DiscountPercent)
admin.site.register(ItemCategory)
