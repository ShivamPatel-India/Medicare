"""Emed URL Configuration

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
from django.urls import path,include
from . import views
# from .views import instruments

urlpatterns = [
    path("findDr/",views.findDr,name="findDr"),
    path("findDr/drview/<int:drid>",views.drview,name="drview"),
    path("findDr/cnview/<int:cnid>",views.cnview,name="cnview"),
    path("findDr/prview/<int:prid>",views.prview,name="prview"),
    path("DrSearch/",views.DrSearch,name="DrSearch"),
    path("emergency/",views.emergency,name="emergency"),
]
