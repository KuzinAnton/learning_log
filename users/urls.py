"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

"""Определяет схемы URL для пользователей."""
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from . import views

#from django.urls import path, include

#app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    #path('', include('django.contrib.auth.urls')),
	#path(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='users'),
    # Registration page.
    #path('register/', views.register, name='register'),
	#url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login')
	#url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='users')
	url(r'^login/$', LoginView.as_view(template_name = 'users/login.html'), name="login"),
]
