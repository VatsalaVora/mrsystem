"""movie URL Configuration

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
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('call', views.call, name='call'),
    path('', views.land, name='land'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('recommend_movies', views.recommend_movies, name='recommend_movies'),
    path('action', views.action, name='action'),
    path('comedy', views.comedy, name='comedy'),
    path('horror', views.horror, name='horror'),
    path('logout', views.logoutuser, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

