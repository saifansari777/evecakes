from django.shortcuts import render
from .models import Item, BannerImage, DealOfTheDay, ItemCategory
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
	banner_image = BannerImage.objects.all()[0]
	dealoftheday = DealOfTheDay.objects.all()[0]

	context = {
				"banner_image": banner_image,
				"doftd": dealoftheday,
				}

	return render(request, 'core/index.html', context)


def banner(request):
	if BannerImage.objects.all()[0]:
		banner_image = BannerImage.objects.all()[0]
	else:
		banner_image = {}
	if DealOfTheDay.objects.all()[0]:
		dealoftheday = DealOfTheDay.objects.all()[0]
	else:
		dealoftheday = {}
	
	context = {
				"banner_image": banner_image,
				"doftd": dealoftheday,
				}
	return render(request, 'core/trash.html', context)


class ItemList(ListView):
	model = Item
	paginate_by =16
	template_name = 'core/itemlist.html'


	def get_context_data(self,**kwargs):
		context = super(ItemList,self).get_context_data(**kwargs)
		if ItemCategory.objects.all().count() > 4:
			context['item_category'] = ItemCategory.objects.all()[:4]
			context['item_category_extra'] = ItemCategory.objects.all()[4:]
		else:
			context['item_category'] = ItemCategory.objects.all()
		return context

class ItemDetail(DetailView):
	model = Item
	template_name = 'core/itemdetail.html'