from django.shortcuts import render,redirect
from django.contrib import messages
import re
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

def valid_pass(pasw):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern,pasw)

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        cpasw=request.POST['cpasw']

        try:
            User.objects.get(username=uname)
            messages.error(request,'Username is already exits..!')
            return redirect('register')

        except:

            if pasw!=cpasw:
                messages.error(request,'Password and Confirm Password is not matching..!')
                return redirect('register')
            
            if not valid_pass(pasw):
                messages.error(request,'Enter Password is not Strong!...\n It must contains smaller,Upper,digits and special Character..')
                return redirect('register')

            user= User.objects.create_user(
                first_name=request.POST['fname'],
                last_name=request.POST['lname'],
                email=request.POST['email'],
                username=uname,
                password=pasw
            )
            ProfilePic.objects.create(
                user=user
            )
            return redirect('login_')
    return render(request,'register.html')

def login_(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        uname=request.POST['uname']
        pasw=request.POST['pasw']
        user=authenticate(username=uname,password=pasw)
        print(user)
        if user:
            login(request,user)
            return redirect('home')
            messages.success(request,'login successfull !')
        else :
            messages.error(request,'enter username or password is incorrect')
            return redirect('login_')
    return render(request,'login_.html')

def logout_(request):
    logout(request)
    messages.success(request,'Logout successfull!')
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):
    profile=ProfilePic.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile})

@login_required(login_url='login_')
def reset_pasw(request):
    if request.method == 'POST':
        if 'old_pasw' in request.POST:
            old_pasw=request.POST['old_pasw']
            user = authenticate(username=request.user,password=old_pasw)
            if user :
                messages.success(request,'Enter new password..!')
                return render(request,'reset_pasw.html',{'new':True})
            else:
                messages.error(request,'Entered Old password is incorrect..!')
                return redirect('reset_pasw')
        if 'new_pasw' in request.POST:
            new_pasw=request.POST['new_pasw']
            con_pasw=request.POST['con_pasw']
            a=User.objects.get(username=request.user)

            if new_pasw !=con_pasw:
                messages.error(request,'New Password and Confirm Password is Not matching...!')
                return redirect('reset_pasw')
            
            if a.check_password(new_pasw):
                messages.error(request,'Entered New Password is already exist..!')
                return redirect('reset_pasw')
            
            a.set_password(new_pasw)
            a.save()
            messages.success(request,'password updated successfully...!')
            return redirect('login_')
    return render(request,'reset_pasw.html')

@login_required(login_url='login_')
def updateprofile(request):
    profile=ProfilePic.objects.get(user=request.user)
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        pic=request.FILES.get('pic')
        user.save()
        profile.profile_pic=pic
        profile.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    return render(request,'updateprofile.html')

def forget_pasw(request):
    if request.method=='POST':
        if 'uname' in request.POST:
            uname=request.POST['uname']
            try:
                a=User.objects.get(username=uname)
                request.session['fp_user']=a.username
                messages.success(request,'Enter new Password')
                return render(request,'forget_pasw.html',{'new':True,'uname':a})
            except:
                messages.error(request,'Username doesnt exist..!')
                return redirect('forget_pasw')
        if 'new_pasw' in request.POST:
            new_pasw=request.POST['new_pasw']
            con_pasw=request.POST['con_pasw']
            user=request.session['fp_user']
            data=User.objects.get(username=user)

            if new_pasw !=con_pasw:
                messages.error(request,'New Password and Confirm Password is Not matching...!')
                return redirect('forget_pasw')
            
            if data.check_password(new_pasw):
                messages.error(request,'Entered New Password is already exist..!')
                return redirect('forget_pasw')
            
            data.set_password(new_pasw)
            data.save()
            messages.success(request,'Password changed Successfully')
            return redirect('login_')
    return render(request,'forget_pasw.html')