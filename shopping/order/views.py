from django.shortcuts import render
from order.models import Cart, Order
from order.forms import OrderInfoForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def cart(request):
	cart_items = Cart.objects.filter(user=request.user)
	total_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		total_price += tmp
	return render(request, "order/cart.html", {
		'cart_items':cart_items,
		'total_price':total_price,
		'message':'카트 상세보기',
	})

def cart_update(request):
	if request.method=="POST":
		return render(request, "item/index.html", {
			'message':'post 로 옴',
			})
	else:
		return HttpResponseRedirect(reverse("cart"))	

def order_info(request):
	cart_items = Cart.objects.filter(user=request.user)
	item_price = 0
	for cart_item in cart_items:
		tmp = cart_item.sub_total_price()
		item_price += tmp
	orderinfoform = OrderInfoForm()
	cart_id = cart_item.cart_id
	delivery_price=2500
	total_price = item_price+delivery_price
	point_made = int(item_price*0.05)
	return render(request, "order/order_info.html", {
		'orderinfoform':orderinfoform,
		'cart_id':cart_id,
		'cart_items':cart_items,
		'item_price':item_price,
		'delivery_price':delivery_price,
		'total_price':total_price,
		'point_made':point_made,
		'message':'주문 정보 입력',
	})
