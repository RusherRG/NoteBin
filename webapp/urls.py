from django.urls import path, include
from . import views

urlpatterns = [ 
    path('submit/', views.submit, name = 'submit'),
    path('login/', views.login, name='login'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home')    
]