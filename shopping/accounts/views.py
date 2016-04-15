from django.shortcuts import render, redirect
from accounts.forms import SignupForm, MypageForm
from accounts.models import Profile

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.views import login as default_login_view

def login(request):
	return default_login_view(request, template_name="accounts/login.html")

def logout(request):
	logout_user(request)
	return redirect("index")

def mypage(request):
	message='get method'
	if request.method == "POST":
		test='post'
		mypageform=MypageForm(request.POST)
		if mypageform.is_valid():
			profile = Profile.objects.get(user=request.user)
			profile.city = mypageform.cleaned_data['city']
			profile.address = mypageform.cleaned_data['address']
			profile.phone = mypageform.cleaned_data['phone']
			profile.save()
			user=request.user
			user.first_name = mypageform.cleaned_data['first_name']
			user.save()
			message = 'updated'
		else:
			message = mypageform.errors
	user=User.objects.get(id=request.user.id)
	mypageform = MypageForm({'first_name':request.user.first_name ,'city':user.profile.city,'address':user.profile.address, 'phone':user.profile.phone})
	context={'message':message,'point':user.profile.point, 'mypageform':mypageform}
	return render(request,"accounts/mypage.html", context)

def signup(request):
	if request.method=="POST":
		userform = SignupForm(request.POST)
		if userform.is_valid():
			user = userform.save(commit=False)
			user.username = userform.cleaned_data['username']
			user.save()
			profile = Profile(user=user)
			profile.save()
			return HttpResponseRedirect(reverse("signup_ok"))	
		return render(request, "accounts/signup.html", {
			'userform': userform,
			'message':'에러발생',
		})
	elif request.method=="GET":
		userform = SignupForm()
		return render(request, "accounts/signup.html", {
			'userform':userform,
			'message':'첫 화면',
		})