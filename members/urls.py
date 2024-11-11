from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('loginpage/',views.member_login,name='loginpage'),
    path('registerpage/',views.member_register,name='registerpage'),
    path('profilpage/',views.member_profile,name='profilpage'),
    path('editpage/',views.member_edit,name='editpage'),
    path('logout/',views.logout_view,name='logout'),

]