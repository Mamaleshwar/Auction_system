"""auctionrush URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from auctions import views as auctions_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', auctions_views.index, name="index"),
    path('myauctions/', auctions_views.my_auctions, name="my_auctions"),
    path('mybids/', auctions_views.my_bids, name="my_bids"),
    path('auctions/', include('auctions.urls')),
    path('register/', views.register, name='register'),
    path('loginpage/', auctions_views.loginpage, name='loginpage'),
    path('login/', auth_views.LoginView.as_view(template_name='auctions/login.html'), name='login'),
    url('^logout/',views.logout,name="logout"),
    url('about/',auctions_views.about,name='about'),
    url('Ourteam/',auctions_views.Ourteam,name='Ourteam'),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', auctions_views.Home, name='Home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
