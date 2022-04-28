"""jobs4you URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.login,name='login'),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_index/$',views.user_index,name='user_index'),
    re_path(r'^user_dash/$',views.user_dash,name='user_dash'),
    re_path(r'^user_view_companies/$',views.user_view_companies,name='user_view_companies'),
    re_path(r'^company_dash/$',views.company_dash,name='company_dash'),
]
