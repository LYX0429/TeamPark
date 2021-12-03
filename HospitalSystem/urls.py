"""HospitalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path

from pages.views import home as home_views
from pages.views import table as table_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', home_views.error),
    path('', home_views.index),
    path('index/', home_views.index),
    path('login/', home_views.login),
    path('logout/', home_views.logout),
    path('form/<object_type>/', table_views.form),
    path('form/<object_type>/new/', table_views.new_edit),
    path('form/<object_type>/new/submit/', table_views.new_submit),
    path('form/<object_type>/new/delete/', table_views.new_delete),
    path('form/<object_type>/<int:object_id>/', table_views.edit),
    path('form/<object_type>/<int:object_id>/submit/', table_views.submit),
    path('form/<object_type>/<int:object_id>/delete/', table_views.delete),
]
