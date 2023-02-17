from django.db import models
import datetime


# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, primary_key=True)
    email= models.EmailField(max_length=200,null=True)
    password = models.CharField( max_length=200, null=True )
    wallet = models.CharField( max_length=200, null=True )
    date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    pin = models.CharField(max_length=200, null=True, blank=True  )
    ref = models.CharField(max_length=200, blank=True, null=True)

    active_deposit = models.IntegerField(max_length=200, null=True, blank=True, default=0)
    balance = models.IntegerField(max_length=200, null=True, blank=True, default=0)
    deposit = models.IntegerField(null=True, blank=True, default=0)
    ref_bal = models.IntegerField(null=True, blank=True, default=0)
    t_deposit = models.IntegerField(null=True, blank=True, default=0)


    profit = models.IntegerField(null=True, blank=True, default=0)
    plan = models.CharField(blank=True, max_length=200)
    duration = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    payday = models.DateTimeField(null=True, blank=True,default=datetime.datetime.now() + datetime.timedelta(days=365))

    pay_approve = models.CharField(max_length=200, null=True, blank=True, default=0)
    with_approve = models.CharField(max_length=200, null=True, blank=True)
    l_withraw = models.FloatField(null=True, blank=True, default='0')
    t_profit = models.IntegerField(null=True, blank=True, default='0')
    t_withdraw = models.IntegerField(null=True, blank=True, default='0')

    title = models.CharField(max_length=200, null=True, blank=True, )
    message = models.CharField(max_length=200, null=True, blank=True, )



    def __str__(self):
        return self.name

class History (models.Model):
    user = models.CharField(max_length=200, null=True, blank=True,)
    type = models.CharField(max_length=200, null=True, blank=True,)
    amount = models.CharField(max_length=200, null=True, blank=type,)
    his_date = models.CharField(max_length=200, null=True, blank=type,)
    status = models.CharField(max_length=200, null=True, blank=type, default='pending..')
    date = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())

    def __str__(self):
        return self.user

class Referral (models.Model):
    user = models.CharField(max_length=200, null=True, blank=True,)
    invited = models.CharField(max_length=200, null=True, blank=True,)

    def __str__(self):
        return self.user

class Site(models.Model):
    site = models.CharField(max_length=200, primary_key=True, blank='site',)
    wallet = models.CharField(max_length=200, null=True, blank=True,)
    fb = models.CharField(max_length=200, null=True, blank=True,)
    wh = models.CharField(max_length=200, null=True, blank=True,)
    tele = models.CharField(max_length=200, null=True, blank=True,)
    phone = models.CharField(max_length=200, null=True, blank=True,)
    address = models.CharField(max_length=200, null=True, blank=True,)
    adm_access = models.CharField(max_length=200, null=True, blank=True,)
    mail = models.CharField(max_length=200, null=True, blank=True,)

    def __str__(self):
        return self.site