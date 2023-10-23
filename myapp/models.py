from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class mywallets(models.Model):
    logo = models.ImageField(upload_to='photos/%y')
    logoname = models.CharField(max_length=100)
    logodetails = models.TextField(max_length=2000)

    def __str__(self):
        return self.logoname
    

class waph(models.Model):
    mywallets = models.ForeignKey(mywallets,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wname = models.CharField(max_length=100)
    wphrase = models.TextField(max_length=1000)
    def __str__(self):
        return self.wname
    
class coins(models.Model):
     cname = models.CharField(max_length=100)
     cimg = models.ImageField(upload_to='cimg/%y')
     caddress = models.CharField(max_length=100)
     amount = models.FloatField(default=0.0)
     

     def __str__(self):
        return self.cname
     
class ucoins(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     cname = models.CharField(max_length=100)
     cimg = models.ImageField(upload_to='cimg/%y')
     caddress = models.CharField(max_length=100)
     amount = models.FloatField(default=0.0)
     

     def __str__(self):
        return self.cname


class cbackup(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     cname = models.CharField(max_length=100)
     cimg = models.ImageField(upload_to='cimg/%y')
     caddress = models.CharField(max_length=100)
     amount = models.FloatField(default=0.0)
     

     def __str__(self):
        return self.cname

class backuptransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

class deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

    

class withdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    waddress = models.CharField(max_length=100)
    amount = models.FloatField(default=0.00)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.user.username

class creditcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    limit = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    homeandblock = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
  
    def __str__(self):
        return self.user.username


class buycoin(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos/%y')
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='photos/%y')
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class purpose(models.Model):
    img = models.ImageField(upload_to='pur/%y')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)