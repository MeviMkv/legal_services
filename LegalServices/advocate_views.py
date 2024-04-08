from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages



def VIEW_CASES(request):
    case = Case.objects.filter(status='Approved')
    context = {
        'case': case
    }
    return render(request,'Advocate/view_cases.html', context)


def ACCEPT_CASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Accepted'
    case.save()
    messages.success(request,'Successfully Accepted!')

    return redirect('advocate_case_status')


def CASE_STATUS(request):
    advocate_id = Advocate.objects.get(admin=request.user.id)
    case = Case.objects.filter(status='Accepted', advocate_id=advocate_id)
    context = {
        'case': case
    }
    return render(request,'Advocate/case_status.html', context)

def CLOSE_PPCASES(request, id):
    case = Case.objects.get(id=id)
    case.status = 'Case Closed'
    case.save()
    messages.success(request,'Successfully Completed!')

    return redirect('advocate_case_status')

def CASE_FEES(request):
    if request.method == "POST":
        case_id = request.POST.get('case_id')
        fees = request.POST.get('fees')

        case = Case.objects.get(id=case_id)
        case.cost = fees
        case.status = 'Case Closed, Requesting Fees'
        case.save()
        messages.success(request, "Fee Payments Request Sent Successfully !")
        return redirect('advocate_view_payments')


def CASE_REPORTS(request):
    if request.method == "POST":
        case_id = request.POST.get('case_id')
        comments = request.POST.get('comments')
        file = request.FILES.get('file')

        case = Case.objects.get(id=case_id)

        report = Report(
            case_id=case,
            comments=comments,
            file=file,
        )
        report.save()
        messages.success(request, "Reports are Successfully Saved !")
        return redirect('advocate_view_report')


def VIEW_REPORTS(request):
    advocate = Advocate.objects.get(admin=request.user.id)
    cases = Case.objects.filter(advocate_id=advocate.id)
    reports = Report.objects.filter(case_id__in=cases)
    context = {
        'reports': reports
    }
    return render(request, 'Advocate/view_reports.html', context)



def VIEW_PAYMENTS(request):
    advocate_id = Advocate.objects.get(admin=request.user.id)
    case = Case.objects.filter(advocate_id=advocate_id.id)
    context = {
        'case': case
    }
    return render(request, 'Advocate/view_payments.html', context)


def ADD_NOTIFICATION(request):
    noti = Notification.objects.all()
    context={
        'noti':noti,
    }
    if request.method == "POST":
        content = request.POST.get('content')

        notification = Notification(
            content=content,
        )
        notification.save()
        messages.success(request, "Notification Send !")
        return redirect('add_notification')

    return render(request, 'Advocate/add_notification.html',context)

def DELETE_NOTIFICATION(request,id):
    notification = Notification.objects.filter(id=id)
    notification.delete()
    messages.success(request, "The Notification has been removed successfully !")
    return redirect('add_notification')