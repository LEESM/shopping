from django.shortcuts import render, redirect
from item.models import Category, Brand, Item, ItemOption, ItemQna, ItemReview
from item.forms import ItemReviewForm
from django.contrib.auth.decorators import login_required

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
	item_qnas = ItemQna.objects.filter(item=item)
	review_write = ItemReviewForm()
	item_reviews = ItemReview.objects.filter(item=item)
	context={
		'item':item, 
		'images':images, 
		'item_qnas':item_qnas, 
		'review_write':review_write, 
		'item_reviews':item_reviews,
		}
	return render(request,"item/detail.html", context)

@login_required
def qna_update(request):
	raw = request.POST.get('question')
	lines = raw.split('\n')
	question = '<p>'+'</p><p>'.join(lines)+'</p>'
	raw_secret = request.POST.get('secret')
	if raw_secret:
		secret = True
	else:
		secret = False
	newqna=ItemQna(
		user=request.user, 
		secret=secret,
		item=Item.objects.get(item_id=request.POST.get('item_id')), 
		question=question,
		)
	newqna.save()
	return redirect('/item/detail/?item_id='+newqna.item.item_id)

@login_required
def review_write(request):
	item_id=request.GET.get('item_id')
	item = Item.objects.get(item_id=item_id)
	itemreviewform = ItemReviewForm()
	context={'item':item,'itemreviewform':itemreviewform}
	return render(request,"item/review_write.html", context)

@login_required
def review_update(request):
	itemreviewform = ItemReviewForm(request.POST)
	newreview = ItemReview(
		user=request.user,
		item=Item.objects.get(item_id=request.POST.get('item_id')), 
		score=request.POST.get('score'),
		comment=request.POST.get('comment')
		)
	newreview.save()
	return redirect('/item/detail/?item_id='+newreview.item.item_id)
