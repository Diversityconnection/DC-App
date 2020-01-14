"""travelling URL Configuration

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
from django.urls import path, include
from rest_framework import routers

from client import views as client_views
from search import views as search_views
from tour import views as tour_views
from guide import views as guide_views
from dashboard import views as dashboard_views

from place.viewsets import CityViewSet


router = routers.DefaultRouter()
router.register(r'city', CityViewSet)

urlpatterns = [
    path('', search_views.search, name='search'),
    path('api/', include(router.urls)),
    path('tours/', tour_views.search, name='tour-search'),
    path('guides/', guide_views.search, name='guide-search'),
    path('guides/<int:id>/', guide_views.guide_detail, name='guide-item'),
    path('login/', client_views.login, name='login'),
    path('registration/', client_views.registration, name='registration'),
    path('logout', client_views.logout, name='logout'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('dashboard/guide/', dashboard_views.guide, name='dashboard-guide'),
    path('admin/', admin.site.urls),
]
