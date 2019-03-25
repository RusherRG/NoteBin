from django.urls import path, include
from . import views

urlpatterns = [ 
    # path('signup/', views.signup, name = 'signup'),
    # path('login/', views.loginuser, name='login'), 
    # path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home')    
]