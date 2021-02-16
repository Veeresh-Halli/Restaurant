from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .filters import MenuItem

# Create your views here.

def index(request):
  if request.method == "POST":
    cat = request.POST.get('search')
    menu = Menu.objects.filter(name__icontains=cat)
  else:
      menu = Menu.objects.all()
  username = request.session.get('username', default='Guest')
  category = Category.objects.all()
  
  filter = MenuItem(request.GET, queryset=menu)
  menu = filter.qs
  
  

  
  context = {'username':username, 'category':category, 'menu':menu, 'filter':filter,}

  return render(request, 'index.html',context)

def loginPage(request):
 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('/')
        else:
            messages.error(request,"username or password is incorrect....")
            return redirect('loginpage')
 
    return render(request, 'loginpage.html')

def registerPage(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account successfully created for "+user)
            return redirect('/loginpage')
        else:
            messages.error(request,"Passwords are not matching...")
            return redirect('registerpage')

    context = {'form':form }
    return render(request, 'registerpage.html',context)

def logoutPage(request):
 if request.session.has_key('username'):
    logout(request)
    request.session.flush()
 else:
     return redirect('loginpage')
 return redirect('loginpage')


def cuisineDetail(request,id):
    items = Menu.objects.all().filter(category=id)
    
    context ={'items':items}
    
    return render(request, 'detail.html', context)