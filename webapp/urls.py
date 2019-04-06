from . import views
from django.urls import path,include
from django.conf.urls import url,include

urlpatterns = [ 
    path('login/', views.login, name='login'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    path('', views.home, name='home'),
    path('<str:name>', views.note, name='note'),
    path('new_note/', views.new_note, name='new note'),
    path('add_note/',views.add_note, name='note adder')
]