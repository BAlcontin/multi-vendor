from django.urls import path
from . import views

urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerDeveloper/', views.registerDeveloper, name='registerDeveloper'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('custDashboard/', views.custDashboard, name='custDashboard'),
    path('devDashboard/', views.devDashboard, name='devDashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/',
         views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
