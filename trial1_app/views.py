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

#def addnewuser(request):
    context = {
        'user' : request.session['user.id'],
    }

    return render(request, "success.html")






def CreateNew(request):  
    return HttpResponse("create a placeholder")

#def AppendAuthor(request, id):
    author = Author.objects.get(id=id)
    author.name = request.POST['name']
    author.quote = request.POST['description']
    author.save
    return redirect(f"/success/{author.id}/update")



def editmyaccount(request):
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


    
    
