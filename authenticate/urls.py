"""
URL configuration for authenticate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import  path,include
from django.urls import __path__, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.urls')),
    path('api/users/', include('djoser.urls')), 
    path('api/users/', include('djoser.urls.jwt')),
    path('single_sign/', include('single_sign.urls')),
   

    # path("auth/", include('authentication.urls')),

    # path("single_sign/", include("allauth.urls")),
    # path("single_sign/", include("single_sign.urls")),
    # path('accounts/', include('accounts.urls')),
    # path('land-buyers/', include('land_buyers.urls')),
    # path('land-sellers/', include('land_sellers.urls')),
    # path('lawyers/', include('lawyers.urls')),
    # path('sso/', include('sso.urls')),
]
