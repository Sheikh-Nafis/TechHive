from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import *
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.contrib.auth.decorators import login_required
import time

# Create your views here.

def homepage(request):
    return render(request, 'home/project.html')

def desktop(request):
    desktop = Desktop.objects.all()
    context = {'desktop':desktop}
    return render(request, 'home/1 desktop.html',context)

def laptop(request):
    laptop = Laptop.objects.all()
    context = {'laptop':laptop}
    return render(request, 'home/2 laptop.html',context)

def slider(request):
    return render(request, 'home/slider.html')

def monitor(request):
    monitor = Monitor.objects.all()
    context = {'monitor':monitor}
    return render(request, 'home/3 monitor.html',context)

def accessories(request):
    accessorie = Accessorie.objects.all()
    context = {'accessorie':accessorie}
    return render(request, 'home/4 accessories.html',context)

def gadget(request):
    gadget = Gadget.objects.all()
    context = {'gadget':gadget}
    return render(request, 'home/5 gadget.html',context)

def component(request):
    component = Component.objects.all()
    context = {'component':component}
    return render(request, 'home/6 component.html',context)

def gaming(request):
    game = Game.objects.all()
    context = {'game':game}
    return render(request, 'home/7 gaming.html', context)

def contact(request):
    return render(request,'home/contact us.html')

def hotdeals(request):
    return render(request,'home/hot deals.html')

def hotdeal1(request):
    return render(request,'home/hotdeal1.html')

def hotdeal2(request):
    return render(request,'home/hotdeal2.html')

def hotdeal3(request):
    return render(request,'home/hotdeal3.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1) 
        print(user)
        if user is not None:
            print("User found")
            auth_login(request,user)
            return redirect('homepage')
        else:
            
            print("User not found")
            error = 'Email and password not matched!'
            context = {
                'error' : error
            }
            return render(request, 'home/log in.html', context)
        
    return render(request,'home/log in.html')

@login_required(login_url='login')
def view_logout(request):
    logout(request)
    return redirect("login")

def register(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('Confirm Password')

        if pass1!=pass2:
            messages.error(request, "Your password and confirm password are not Same!!")
            # return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email)
            my_user.set_password(pass1)
            my_user.save()
            return redirect('login')
        
     return render(request,'home/Register.html')

def header(request):
    return render(request, 'home/header.html')

def footer(request):
    return render(request, 'home/footer.html')


@login_required(login_url='login')
def password_change_view(request): 
      
     if request.method=='POST': # This condition is used to ensure that the code inside the if block executes only when the form is submitted.
         username = request.user.username 
         current_password = request.POST['cpass'] 
         print(type(username)) 
         user = authenticate(username=username,password = current_password) 
  
         if user is not None: 
              
             current_user = User.objects.get(username=username) 
              
             password1 = request.POST['pass1'] 
             password2 = request.POST['pass2'] 
              
              
             if password1 == password2: 
                 if current_user.check_password(password1):
                        messages.error(request, "New password cannot be the same as the old password.")
                 else:
                    current_user.set_password(password1)
                    current_user.save()
                    messages.success(request, 'Password changed successfully')
                    logout(request)
                    time.sleep(2)
                    return redirect("login")
             else:
                messages.error(request, "New password and confirm password do not match.")
         else:
            messages.error(request, "Current password does not match.")
      
     return render(request, 'home/password_change.html')

def search(request):
    return HttpResponse("LOL")
