from django.shortcuts import render, get_object_or_404, redirect
from core.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from .models import OrderItem, Order
from django.utils import timezone
from django.contrib import messages
from django.views.generic import View
# Create your views here.


def cart(request):
	return render(request, 'cart/cart.html', {})


@login_required
def add_to_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_item, created = OrderItem.objects.get_or_create(
		item=item,
		user=request.user,
		ordered=False
		)
	order_qs = Order.objects.filter(user=request.user, ordered=False)
	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__slug=item.slug).exists():
			order_item.quantity += 1
			order_item.save()
			messages.success(request, "This item was updated in your Cart")
		else:
			messages.success(request, "This item was added to your Cart")
			order.items.add(order_item)
	else:
		ordered_date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=ordered_date)
		messages.success(request, "This item was added to your Cart")
		order.items.add(order_item)
	return redirect('core:item-detail', slug=slug)

@login_required
def remove_from_cart(request, slug):
	item = get_object_or_404(Item, slug=slug)
	order_qs = OrderItem.objects.filter(user=request.user, ordered=False)

	if order_qs.exists():
		order = order_qs[0]
		if order.items.filter(item__slug=item.slug).exists():
			order_item = OrderItem.objects.filter(
												item=item,
												user=request.user,
												ordered=False
												)[0]
			
			order.items.remove(order_item)
			messages.succes(request, "This item was remove from your Cart")
		else:
			# add a message saying order doesnot contain the item
			messages.info(request, "This item was not in your Cart")
			return redirect('core:item-detail', slug=slug)
	else:
		# add a message saying no orders
		messages.info(request, "Your doesnot have an active order")
		return redirect('core:item-detail', slug=slug)
	return redirect('core:item-detail', slug=slug)


class OrderSummary(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		try:
				order = Order.objects.get(user=self.request.user, ordered=False)
				context = {
						"object": order,
							}
				return render(self.request, 'cart/order_summary.html', context)
		except ObjectDoesNotExist:
			messages.error(self.request, "You do not have an active order")
			return redirect("/")