from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt


def index(request):

    return render(request, 'login.html')


def login(request):

    user, errors = User.objects.login_validate(request.POST)

    if errors:
        for key, error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = user.id
        return redirect("/success")


def register(request):

    errors = User.objects.register_validate(request.POST)

    if errors:
        for key, error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        user = User.objects.create(first_name=request.POST['first_name'],
                                    last_name=request.POST['last_name'],
                                    email=request.POST['email'],
                                    password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())
        request.session['user_id'] = user.id
        return redirect("/success")


def success(request):
    context = {
        'user': User.objects.filter().first()
    }
    return render(request, 'success.html', context)


def newblog(request):
    errors = Blog.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/success')
    
    else:

        Blog.objects.create(author=request.POST['author'], description=reques.POST['description'])
    return redirect(f"/success/{blog.id}")



def edit(request):
    return render(request, 'edit.html')

def addnewuser(request,id):
    user = User.objects.create(first_name=request.POST['first_name'],
                                last_name=request.POST['last_name'],
                                email=request.POST['email'],
                                password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())
    request.session['user_id'] = user.id

    return render(f"/success/{user.id}")


# def like(request, id):
    # context = {
     #   'blog': Blog.objects.creat(id=id)
    # }
    # return render(request, 'success.html', context)

# def CreateNew(request):
 #   return HttpResponse("create a placeholder")
def allblog(request):
    context = {
        
        'blog': Blog.objects.all()
    }
    return render(request, "success.html", context)

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.description = request.POST['description']
    blog.delete
    return redirect(f"/success/{blog.id}/delete")


def blog(request, id):
    context = {
        'user': User.objects.get(id=id),
        'blog' : Blog.objects.get(id=id)
        
    }
    return render(request, 'user.html', context)


                                    
    


def back(request):
    blog = Blog.objects.get(id=id)
    return render(request, 'success.html')





# def updatemyaccount(request, id):
    # user = User.objects.get(id=id)
    # user.first_name = request.POST['first_name']
    # user.last_name = request.POST['last_name']
    # user.save

    # return render(request, "success.html")

def logout(request):
    return render(request, 'login.html')