from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages

def VIEW_ADVOCATE(request):
    advocate = Advocate.objects.filter(public=None)
    #print(student)

    context = {
        'advocate':advocate,
    }
    return render(request, 'Users/view_advocate.html', context)

def ADD_CASE(request):
    if request.method == "POST":
        user_id = Users.objects.get(admin=request.user.id)
        advocate_id = request.POST.get('advocate_id')
        content = request.POST.get('content')

        advocate = Advocate.objects.get(id=advocate_id)

        case = Case(
            user_id = user_id,
            advocate_id=advocate,
            content = content,
            status='Added'
        )

        case.save()
        messages.success(request,"Details are successfully added !")
        return redirect('view_case')
    return render(request, 'Users/add_case.html')


def VIEW_CASE(request):
    users = Users.objects.filter(admin=request.user.id)
    for i in users:
        user_id = i.id
        case = Case.objects.filter(user_id=user_id)
        context = {
            'case': case
        }
    return render(request, 'Users/view_cases.html', context)


def DELETE_CASE(request,id):
    case = Case.objects.filter(id= id)
    case.delete()
    messages.success(request,"The Case has been removed successfully !")
    return redirect('view_case')


def CASE_STATUS(request):
    users = Users.objects.filter(admin=request.user.id)
    for i in users:
        user_id = i.id
        case = Case.objects.filter(user_id=user_id)
        context = {
            'case': case
        }
    return render(request, 'Users/case_status.html', context)


def VIEW_PUBLIC(request):
    advocate = Advocate.objects.filter(public='Yes')
    #print(student)

    context = {
        'advocate':advocate,
    }
    return render(request, 'Users/view_public.html', context)


def ADD_PUBLIC(request):
    if request.method == "POST":
        user_id = Users.objects.get(admin=request.user.id)
        advocate_id = request.POST.get('advocate_id')
        content = request.POST.get('content')
        file = request.FILES.get('file')

        advocate = Advocate.objects.get(id=advocate_id)

        case = Case(
            user_id = user_id,
            advocate_id=advocate,
            content = content,
            file=file,
            status='PP Case Added'
        )

        case.save()
        messages.success(request,"Details are successfully added !")
        return redirect('view_case')
    return render(request, 'Users/add_case.html')

def ADD_FEES(request):
    if request.method == "POST":
        case_id = request.POST.get('case_id')
        case = Case.objects.get(id=case_id)
        case.status = 'Case Closed, Payment Completed'
        case.save()
        messages.success(request, "Fee Payments Completes Sent Successfully !")
        return redirect('users_view_payments')

def VIEW_NOTIFICATION(request):
    noti = Notification.objects.all()
    context={
        'noti':noti,
    }

    return render(request, 'Users/view_notification.html',context)

def VIEW_REPORTS(request):
    users = Users.objects.get(admin=request.user.id)
    cases = Case.objects.filter(advocate_id=users.id)
    reports = Report.objects.filter(case_id__in=cases)
    context = {
        'reports': reports
    }
    return render(request, 'Users/view_reports.html', context)

def VIEW_PAYMENTS(request):
    users = Users.objects.get(admin=request.user.id)
    cases = Case.objects.filter(user_id=users.id,status='Case Closed, Payment Completed')
    context = {
        'case': cases
    }
    return render(request, 'Users/view_payments.html', context)


def ADD_SUGGESTION(request):
    if request.method == "POST":
        user_id = Users.objects.get(admin=request.user.id)
        content = request.POST.get('content')

        feedback = QndA(
            user_id=user_id,
            content=content,
        )
        feedback.save()

        messages.success(request, " Details are successfully added !")
        return redirect('view_suggestion')
    return render(request, 'Users/add_suggestion.html')


def VIEW_SUGGESTION(request):
    users = Users.objects.filter(admin=request.user.id)
    for i in users:
        user_id = i.id
        feedback = QndA.objects.filter(user_id=user_id)
        context = {
            'feedback': feedback
        }

    return render(request, 'Users/view_suggestion.html', context)