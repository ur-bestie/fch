from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signin',views.signin, name='signin'),
    path('signup',views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('link_w',views.link_w, name='link_w'),
    path('con_w/<str:id>',views.con_w, name='con_w'),
    path('fundwallet/<str:id>',views.fundwallet, name='fundwallet'),
    path('withd/<str:id>',views.withd, name='withd'),
    path('wadetails/<str:id>',views.wadetails, name='wadetails'),
    path('mymessages',views.mymessages, name='mymessages'),
    path('reason',views.reason, name='reason'),
    path('card',views.card, name='card'),
    path('myprofile',views.myprofile, name='myprofile'),
    path('withdraw',views.withdraw, name='withdraw'),
    path('backup',views.backup, name='backup'),
    path('profile_update',views.profile_update, name='profile_update'),
    path('buy_coin',views.buy_coin, name='buy_coin'),
   
]

