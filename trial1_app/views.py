from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

def index(request):
    
    return render(request, 'login.html')

def login(request):

    user, errors = User.objects.login_validate(request.POST)

    if errors:
        for key,error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = user.id
        return redirect("/success")

def register(request):
    
    errors = User.objects.register_validate(request.POST)

    if errors:
        for key,error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        user = User.objects.create(first_name=request.POST['first_name'], 
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email'],
                                    password=bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode())
        request.session['user_id'] = user.id
        return redirect("/success")
    


def success(request):
    context = {
        "user" : User.objects.filter().first
    }
    return render(request, 'success.html', context)

def process_new(request):
    errors = Blog.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
            
        return redirect ('/blog/edit/'+id)
    else:
        
        Blog.objects.create(user=user,description=reques.POST['description'])
    return redirect('./')

#def addnewuser(request):
#    context = {
 # }

   # return render(request, "success.html",context)


#def like(request, id):
    #context = {
     #   'blog': Blog.objects.creat(id=id)
    #}    
    #return render(request, 'success.html', context)



#def CreateNew(request):  
 #   return HttpResponse("create a placeholder")

def AppendBlog(request, id):
    blog = Blog.objects.get(id=id)
    blog.name = request.POST['name']
    blog.description = request.POST['description']
    blog.save
    return redirect(f"/success/{blog.id}/update")

def blog(request, id):
    context = {
        'blog' : Blog.objects.get(id=id)
    }
    return render(request, 'user.html', context)
    


def edit(request,id):
    context = {
        'users': User.objects.get(request.session['user_id'])
    }
    return render(request, "edit.html", context)


def updatemyaccount(request, id):
    user = User.objects.get(id=id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save
    
    return render(request, "success.html")
    

def logout(request):
    return render(request, 'login.html')


    
    
