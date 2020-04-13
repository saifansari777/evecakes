from django.shortcuts import render
from .models import Cake, BannerImage, DealOfTheDay
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
	if BannerImage.objects.all()[0].exists():
		banner_image = BannerImage.objects.all()[0]
	else:
		banner_image = {}
	if DealOfTheDay.objects.all()[0].exists():
		dealoftheday = DealOfTheDay.objects.all()[0]
	else:
		dealoftheday = {}
	
	context = {
				"banner_image": banner_image,
				"doftd": dealoftheday,
				}
	return render(request, 'core/trash.html', context)




class CakeList(ListView):
    model = Cake
    template_name = 'core/cakelist.html'


class CakeDetail(DetailView):
    model = Cake
    template_name = 'core/cakedetail.html'