from django.contrib import admin
from .models import Member, History, Referral,Site

# Register your models here.
admin.site.register(Member)
admin.site.register(History)
admin.site.register(Referral)
admin.site.register(Site)

