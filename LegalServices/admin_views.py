from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages


#Advocate Modules
@login_required(login_url='/')
def ADD_ADVOCATE(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        regno = request.POST.get('regno')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, ' email is already taken')
            return redirect('add_advocate')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, ' Username is already taken')
            return redirect('add_advocate')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()

            advocate = Advocate(
                admin=user,
                address=address,
                gender=gender,
                regno=regno,
            )
            advocate.save()
            messages.success(request," Details of" + user.first_name + " " + user.last_name + " are Successfully Saved !" )
            return redirect('view_advocate')

    return render(request,'Admin/add_advocate.html')


def VIEW_ADVOCATE(request):
    advocate = Advocate.objects.all()
    #print(student)

    context = {
        'advocate':advocate,
    }
    return render(request, 'Admin/view_advocate.html', context)

def PUBLIC_ADVOCATE(request, id):
    advocate = Advocate.objects.get(id=id)
    advocate.public = 'Yes'
    advocate.save()
    messages.success(request,'Public Prosecutor Status Added Successfully !')

    return redirect('view_advocate')

def EDIT_ADVOCATE(request,id):
    advocate = Advocate.objects.filter(id = id)

    context = {
        'advocate':advocate,
    }
    return render(request,'Admin/edit_advocate.html', context)


def UPDATE_ADVOCATE(request):
    if request.method == "POST":

        advocate_id = request.POST.get('advocate_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        #print(profile_pic)

        user = CustomUser.objects.get(id=advocate_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        advocate = Advocate.objects.get(admin=advocate_id)
        advocate.address = address
        advocate.gender = gender
        advocate.save()

        messages.success(request, "records of" + " " + user.first_name +" "+ user.last_name +" "+ "are succesfully updated !")
        return redirect('view_advocate')
    return render(request, 'Admin/edit_advocate.html')


def DELETE_ADVOCATE(request, admin):
    advocate = CustomUser.objects.filter(id=admin)
    advocate.delete()
    messages.success(request,'Records are successfully Deleted !')

    return redirect('view_advocate')

#Advisor Modules
@login_required(login_url='/')
def ADD_ADVISOR(request):

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, ' email is already taken')
            return redirect('add_advocate')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, ' Username is already taken')
            return redirect('add_advocate')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=4
            )
            user.set_password(password)
            user.save()

            advisor = Advisor(
                admin=user,
                address=address,
                gender=gender,
            )
            advisor.save()
            messages.success(request," Details of" + user.first_name + " " + user.last_name + " are Successfully Saved !" )
            return redirect('view_advisor')

    return render(request,'Admin/add_advisor.html')


def VIEW_ADVISOR(request):
    advisor = Advisor.objects.all()
    #print(student)

    context = {
        'advisor':advisor,
    }
    return render(request, 'Admin/view_advisor.html', context)


def EDIT_ADVISOR(request,id):
    advisor = Advisor.objects.filter(id = id)

    context = {
        'advisor':advisor,
    }
    return render(request,'Admin/edit_advisor.html', context)


def UPDATE_ADVISOR(request):
    if request.method == "POST":

        advisor_id = request.POST.get('advisor_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        #print(profile_pic)

        user = CustomUser.objects.get(id=advisor_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()

        advisor = Advisor.objects.get(admin=advisor_id)
        advisor.address = address
        advisor.gender = gender
        advisor.save()

        messages.success(request, "records of" + " " + user.first_name +" "+ user.last_name +" "+ "are succesfully updated !")
        return redirect('view_advocate')
    return render(request, 'Admin/edit_advisor.html')


def DELETE_ADVISOR(request, admin):
    advisor = CustomUser.objects.filter(id=admin)
    advisor.delete()
    messages.success(request,'Records are successfully Deleted !')

    return redirect('view_advocate')


def VIEW_CASES(request):
    case = Case.objects.filter(status='Added')
    context = {
        'case': case
    }
    return render(request, 'Admin/view_cases.html', context)


def CASE_STATUS(request):
    case = Case.objects.all()
    context = {
        'case': case
    }
    return render(request,'Admin/case_status.html', context)

def APPROVE_CASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Approved'
    case.save()
    messages.success(request,'Records are successfully Approved!')

    return redirect('admin_case_status')

def REJECT_CASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Rejected'
    case.save()
    messages.success(request,'Records are successfully Rejected !')

    return redirect('admin_case_status')

def VIEW_PPCASES(request):
    case = Case.objects.filter(status='PP Case Added')
    context = {
        'case': case
    }
    return render(request, 'Admin/view_ppcases.html', context)


def CASE_PPSTATUS(request):
    case = Case.objects.all()
    context = {
        'case': case
    }
    return render(request,'Admin/case_status.html', context)

def APPROVE_PPCASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Approved'
    case.save()
    messages.success(request,'Records are successfully Approved!')

    return redirect('admin_case_status')

def REJECT_PPCASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Rejected'
    case.save()
    messages.success(request,'Records are successfully Rejected !')

    return redirect('admin_case_status')


def VIEW_PAYMENTS(request):
    case = Case.objects.all()
    context = {
        'case': case
    }
    return render(request, 'Admin/view_payments.html', context)