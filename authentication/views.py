from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from foundation.models import Complaint
from authentication.forms import UserForm,UserProfileForm
from datetime import datetime
# Create your views here.

def index(request):
    title = "Homepage"
    complains=Complaint.objects.all()
    return render(request,"index.html",{'title':title,'complains':complains})

#Function get ip address of user
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def _loginpage(request):
	return render(request,'auth/login.html',{'title':"Login"})

def _login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.info(request,"Welcome "+user.username)
                return HttpResponseRedirect('/dashboard')
            else:
                messages.warning(request,"User is inactive. Contact webmaster!")
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,"Invalid username/password.")
            return HttpResponseRedirect('/login')

# def signup(request):
#     registered=False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save(commit=False)
#             user.set_password(user.password)
#             user.is_active=True
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.lastLoginDate = datetime.now()
#             profile.ipaddress=get_client_ip(request)
#             if request.FILES['picture']:
#                 profile.picture = request.FILES['picture']
#             profile.save()
#             registered = True
#         else:
#             print user_form.errors, profile_form.errors,request.POST
#             messages.info(request,str(user_form.errors)+str(profile_form.errors))
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#     return render(request,'auth/signup.html',{'title':"Signup",'userform':user_form,'profileform':profile_form,'registered':registered})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        email = request.POST.get('email',"")
        firstname = request.POST.get('firstname',"")
        lastname = request.POST.get('lastname',"")
        user = User.object.create_user(username,email,password)
        user.first_name = firstname
        user.lastname = lastname
        user.save()
        messages.info(request,"Successfully registered")
        return HttpResponseRedirect('/')
def _logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    return render(request,'index.html',{'title':"Dashboard"})
    # Should render dashboard.html template, index is used for temp workaround