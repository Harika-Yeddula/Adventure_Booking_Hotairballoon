"""Hotairballonbooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    #ADMIN URL
    path("admin/", admin.site.urls),

    #HOMEPAGE URL
    path('', views.homepage, name="homepage"),

    #LOGIN,LOGOUT AND SIGNUP URLS
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('logout/',views.logoutuser,name="logoutuser"),


    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),

    path('mybookings/',views.mybookings,name="mybookings"),
    path('searchlocation/',views.searchlocation,name="searchlocation"),
    path('booking/', views.booking, name="booking"),
    path('editbooking/<int:id>', views.editbooking, name="editbooking"),
    path('deletebooking/<int:id>', views.deletebooking, name="deletebooking"),

    path('test/', views.test, name="test"),

    #PASSWORD RESET URLS

    # Submit email form
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),

    #Email sent success message
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),

    #Link to password reset form in email
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),

    #password successfully changed message
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

]
