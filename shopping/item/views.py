from django.shortcuts import render
from .models import Category, Brand, Item, ItemOption

def index(request):
	items = Item.objects.all()
	context={'items':items}
	return render(request,"item/index.html", context)

def detail(request):
	item_id=request.GET.get('item_id')
	item=Item.objects.get(item_id=item_id)
	images = []
	images.append(item.image0)
	if(item.image1!=''):
		images.append(item.image1)
	if(item.image2!=''):
		images.append(item.image2)
	if(item.image3!=''):
		images.append(item.image3)
	if(item.image4!=''):
		images.append(item.image4)
	if(item.image5!=''):
		images.append(item.image5)
	if(item.image6!=''):
		images.append(item.image6)
	if(item.image7!=''):
		images.append(item.image7)
	if(item.image8!=''):
		images.append(item.image8)
	if(item.image9!=''):
		images.append(item.image9)
	context={'item':item, 'images':images}
	return render(request,"item/detail.html", context)

