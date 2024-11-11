from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('recopage/',views.reco,name='recopage'),
    ]