from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from demoapp import views


app_name='demoapp'

urlpatterns = [
    path('dash/',views.dash,name='dash'),
    path('org/',views.org_form,name='org_form'),
    path('Adm',views.admin_form,name='admin_form'),
    path('emp/',views.emp_form,name='emp_form'),
    path('mng/',views.mang_form,name='mang_form'),
    path('task/',views.task_form,name='task_form'),
    path('work/',views.work_form,name='work_form'),
    path('dep/',views.dep_form,name='dep_form'),
    path('clients/',views.client_form,name='client_form'),
    path('dash2/',views.client_detail_view,name='dash2'),
    path('dash3/',views.dash3,name='dash3'),
    path('dash4/',views.dash4,name='dash4'),
    path('dash5/',views.dash5,name='dash5'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('profile/<str:pk>/',views.client_profile_view,name='profile'),
]