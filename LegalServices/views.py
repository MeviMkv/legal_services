from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser, Users
from django.contrib.auth.decorators import login_required




def BASE(request):
    return render(request,'base.html')

def LANDING(request):
    return render(request,'index.html')

def LOGIN(request):
    return render(request,'login.html')


def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                       username=request.POST.get('email'),
                                       password=request.POST.get('password'),)
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_view_case')
            elif user_type == '2':
                return redirect('advocate_view_case')
            elif user_type == '3':
                return redirect('user_view_advocate')
            elif user_type == '4':
                return redirect('advisor_view_suggestion')
            else:
                messages.error(request,'Email and Password are Invalid !')
                return redirect('login')
        else:
            messages.error(request, 'Email and Password are Invalid !')
            return redirect('login')


def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    print(user)

    context={
        "user":user,
    }
    return render(request,'profile.html',context)

@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name=request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(profile_pic,first_name,last_name,email,username,password)
        #print(profile_pic)
        try:
            customuser=CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name


            if password !=None and password != "":
                 customuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                 customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'failed to update your profile !')
    return render(request, 'profile.html')


def ADD_USER(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')


        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'email is already taken')
            return redirect('add_user')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken')
            return redirect('add_user')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()

            consumer = Users(
                admin=user,
                address=address,
                gender=gender,
                phone = phone,
            )
            consumer.save()
            messages.success(request,"User Details of" + user.first_name + " " + user.last_name + " are Successfully Saved !" )
            return redirect('login')

    return render(request,'register.html')


