from django.urls import path
from . import views

# all my urls
urlpatterns = [

    path('', views.index),
    path('ref/', views.ref),
    path('about/', views.about),
    path('livepay/', views.livepay),
    path('terms/', views.terms),
    path('faq/', views.faq),
    path('signup/', views.signup),
    path('login/', views.login),
    path('account/', views.account),
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw),
    path('history/', views.history),
    path('settings/', views.settings),
    path('security/', views.security),
    path('site/', views.site),
    path('pin/', views.pin),
    path('admin/', views.admin),
    path('logout/', views.logout)


]