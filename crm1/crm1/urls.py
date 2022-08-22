"""crm1 URL Configuration

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

from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def page1(request):
    return HttpResponse("<h1>Page1</h1>")  # Page 

def page2(request):
    return(HttpResponse("page2"))

urlpatterns = [
    # Don't Forget , after each line
    path('admin/', admin.site.urls),
    path('', home) , # Landing page just the domain name www.main.com
    path('page1/', page1),
    path('page2/', page2), 
]

