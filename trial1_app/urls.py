from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('process_new',views.process_new,name='process_new'),
    #path('CreateNew', views.CreateNew, name='CreateNew'),
    path('AppendBlog', views.AppendBlog, name='AppendBlog'),
    path('blog', views.blog, name='blog'),
    #path('addnewuser', views.addnewuser, name='addnewuser'),
    path('delete', views.delete, name='delete'),
    path('<int:number>', views.blog, name='blog'),
    path('edit', views.edit, name='edit'),
    path('back', views.back, name='back'),
    #path('userquote', views.userquote, name='userquote'),
    path('logout', views.logout, name="logout"),
]