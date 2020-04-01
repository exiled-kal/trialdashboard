from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    #path('addnewuser', views.addnewuser, name='addnewuser'),
    path('editmyaccount', views.editmyaccount, name='editmyaccount'),
    path('AppendAuthor', views.AppendAuthor, name='AppendAuthor'),
    #path('userquote', views.userquote, name='userquote'),
    path('logout', views.logout, name="logout"),
]