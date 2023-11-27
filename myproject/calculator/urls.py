from django.urls import path
from .views import hello
from .views import calc, get_users,add_user,login

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc',calc),
    path('user',get_users),
    path('add_user',add_user),
    path('login',login),
]
