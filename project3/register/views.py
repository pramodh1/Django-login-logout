from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login1(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username ,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
           
        else:
            messages.info(request,'invalid details')
            return redirect('login1')    


    else:
        return render(request,'login1.html')    


def registration(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')    
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('registration')
                
            else:
                user =User.objects.create_user(username=username,password=password1,email=email,first_name
                =first_name,last_name=last_name)
                user.save()
                return redirect('login1')
        else:
            messages.info(request,"password not matching")
            return redirect('registration')

    else:
        return render(request,'register.html')    
def logout(request):
    auth.logout(request)
    return redirect('/')