"""
URL configuration for LegalServices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, admin_views, users_views, advocate_views, advisor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LANDING, name='landing'),

    #login_Path
    path('login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='doLogout'),
    path('SignUp/', views.ADD_USER, name='add_user'),

    #profile update
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    #HOD panel URL
    path('Admin/Advocate/Add', admin_views.ADD_ADVOCATE, name='add_advocate'),
    path('Admin/Advocate/View', admin_views.VIEW_ADVOCATE, name='view_advocate'),
    path('Admin/Advocate/Public/<str:id>', admin_views.PUBLIC_ADVOCATE, name='public_advocate'),
    path('Admin/Advocate/Edit/<str:id>', admin_views.EDIT_ADVOCATE, name='edit_advocate'),
    path('Admin/Advocate/Update', admin_views.UPDATE_ADVOCATE, name='update_advocate'),
    path('Admin/Advocate/Delete/<str:admin>',admin_views.DELETE_ADVOCATE, name='delete_advocate'),

    path('Admin/Advisor/Add', admin_views.ADD_ADVISOR, name='add_advisor'),
    path('Admin/Advisor/View', admin_views.VIEW_ADVISOR, name='view_advisor'),
    path('Admin/Advisor/Edit/<str:id>', admin_views.EDIT_ADVISOR, name='edit_advisor'),
    path('Admin/Advisor/Update', admin_views.UPDATE_ADVISOR, name='update_advisor'),
    path('Admin/Advisor/Delete/<str:admin>',admin_views.DELETE_ADVISOR, name='delete_advisor'),

    path('Admin/Cases/View', admin_views.VIEW_CASES, name='admin_view_case'),
    path('Admin/Case/Status', admin_views.CASE_STATUS, name ='admin_case_status'),
    path('Admin/Cases/Approve/<str:id>', admin_views.APPROVE_CASES, name='approve_case'),
    path('Admin/Case/Reject/<str:id>', admin_views.REJECT_CASES, name ='reject_case'),

    path('Admin/PPCases/View', admin_views.VIEW_PPCASES, name='admin_view_ppcase'),
    path('Admin/PPCases/Status', admin_views.CASE_PPSTATUS, name ='admin_ppcase_status'),
    path('Admin/PPCases/Approve/<str:id>', admin_views.APPROVE_PPCASES, name='approve_ppcase'),
    path('Admin/PPCases/Reject/<str:id>', admin_views.REJECT_PPCASES, name ='reject_ppcase'),

    path('Admin/Case/Payments', admin_views.VIEW_PAYMENTS, name ='admin_view_payments'),



    path('Advocate/Cases/View', advocate_views.VIEW_CASES, name='advocate_view_case'),
    path('Advocate/Cases/Status', advocate_views.CASE_STATUS, name='advocate_case_status'),
    path('Advocate/Cases/Reports', advocate_views.CASE_REPORTS, name='add_report'),
    path('Advocate/Cases/ClosePPCase/<str:id>', advocate_views.CLOSE_PPCASES, name='close_ppcase'),
    path('Advocate/Cases/Fees', advocate_views.CASE_FEES, name='add_fee'),
    path('Advocate/Cases/Reports_View', advocate_views.VIEW_REPORTS, name='advocate_view_report'),
    path('Advocate/Cases/Payments', advocate_views.VIEW_PAYMENTS, name='advocate_view_payments'),
    path('Advocate/Cases/Approve/<str:id>', advocate_views.ACCEPT_CASES, name='accept_case'),
    path('Advocate/Notifications/Add', advocate_views.ADD_NOTIFICATION, name='add_notification'),
    path('Advocate/Notifications/Delete/<str:id>', advocate_views.DELETE_NOTIFICATION, name='delete_notification'),



    path('User/Advoactes/View', users_views.VIEW_ADVOCATE, name='user_view_advocate'),
    path('User/Advoactes/PP', users_views.VIEW_PUBLIC, name='user_view_public'),
    path('User/Cases/View', users_views.VIEW_CASE, name='view_case'),
    path('User/Cases/Add', users_views.ADD_CASE, name='add_case'),
    path('User/Cases/Add_PP', users_views.ADD_PUBLIC, name='add_public'),
    path('User/Case/Delete/<str:id>', users_views.DELETE_CASE, name='delete_case'),
    path('User/Case/Status', users_views.CASE_STATUS, name ='case_status'),
    path('User/Cases/Fees', users_views.ADD_FEES, name='add_payment'),
    path('User/Case/Payments', users_views.VIEW_PAYMENTS, name ='users_view_payments'),
    path('User/Notifications/View', users_views.VIEW_NOTIFICATION, name='view_notification'),
    path('User/Cases/Reports_View', users_views.VIEW_REPORTS, name='view_report'),
    path('User/Feedback/Add', users_views.ADD_SUGGESTION, name='add_suggestion'),
    path('User/Feedback/View', users_views.VIEW_SUGGESTION, name='view_suggestion'),



    path('Advisor/Suggestions/View', advisor_views.VIEW_SUGGESTION, name='advisor_view_suggestion'),
    path('Advisor/Suggestions/Reply', advisor_views.REPLY_SUGGESTION, name='reply_suggestion'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
