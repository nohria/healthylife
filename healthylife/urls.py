"""healthylife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from lifestyle.views import *
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('app/',app),
    path('about/',about),
    path('services/',services),
    path('diet/',diet),
    path('contect/',contectpage),
    path('blog/',blog),
    path('recipes/',recipes),
    path('breakfast/',breakfast),
    path('lunch/',lunch),
    path('snacks/',snacks),
    path('dinner/',dinner),

    path('blogdetals/<int:id>',blogdetals),
    path('apply/',apply , name='apply'),
    path('suba/',suba , name='suba'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('sign/', sign),
 
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
