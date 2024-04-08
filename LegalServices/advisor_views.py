from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import *
from django.contrib import messages

def VIEW_SUGGESTION(request):
    suggestion = QndA.objects.all()
    context = {
        'suggestion': suggestion
    }
    return render(request, 'Advisor/view_suggestion.html', context)


def REPLY_SUGGESTION(request):
    if request.method == "POST":
        advisor = Advisor.objects.get(admin=request.user.id)
        feedback_id = request.POST.get('feedback_id')
        reply = request.POST.get('reply')

        suggestion = QndA.objects.get(id=feedback_id)
        suggestion.reply = reply
        suggestion.advisor_id = advisor
        suggestion.save()
        messages.success(request, "Suggestion reply Send !")
        return redirect('advisor_view_suggestion')
    return render(request, 'Advisor/view_suggestion.html')

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