"""Alt_Career URL Configuration

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
from django.urls import path
from .views import options_skill0, options_skill1, options_skill2, options_skill3, options_skill4, options_skill5, options_skill6, home, result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skills/', options_skill0.as_view()),
    path('skill1/', options_skill1.as_view()),
    path('skill2/', options_skill2.as_view()),
    path('skill3/', options_skill3.as_view()),
    path('skill4/', options_skill4.as_view()),
    path('skill5/', options_skill5.as_view()),
    path('skill6/', options_skill6.as_view()),
    path('', home),
    path('recommend/', result)
]
