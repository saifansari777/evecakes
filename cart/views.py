from django.shortcuts import render, get_object_or_404, redirect
from core.models import Cake
from .models import OrderItem, Order
from django.utils import timezone
from django.contrib import messages
# Create your views here.


def cart(request):
	return render(request, 'cart/cart.html', {})

def add_to_cart(request, slug):
	item = get_object_or_404(Cake, slug=slug)
	order_item = OrderItem.objects.get_or_create(
		item=item,
		user=request.user,
		ordered=False
		)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item was updated in your Cart")
		else:
			messages.info(request, "This item was added to your Cart")
			order.items.add(order_item)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		messages.info(request, "This item was added to your Cart")
		order.items.add(order_item)
	return redirect('core:cake-detail', slug=slug)


def remove_from_cart(request, slug):
	item = get_object_or_404(Cake, slug=slug)
	order_qs = OrderItem.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__id=item.id).exists():
			order_item = OrderItem.objects.filter(
												item=item,
												user=request.user,
												ordered=False
												)[0]
			
			order.items.remove(order_item)
			messages.info(request, "This item was remove to your Cart")
		else:
			# add a message saying order doesnot contain the item
			messages.info(request, "This item was not in your Cart")
			return redirect('core:cake-detail', slug=slug)
	else:
		# add a message saying no orders
		messages.info(request, "Your doesnot have an active order")
		return redirect('core:cake-detail', slug=slug)
	return redirect('core:cake-detail', slug=slug)	