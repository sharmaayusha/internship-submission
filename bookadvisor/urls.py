"""bookadvisor URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as tview
from main import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('book_api1', views.book_api,basename="bookapi"),


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('register/',views.registration_view),
                  path('logout/', views.logout,name="logout"),
                  path('book_api/',views.book_api,name="bookapi"),
                  path('fav_api/',views.fav_api,name="favapi"),
                  path('fav_api/<int:pk>',views.fav_api,name="favapiint"),
                  path('book_api/<int:pk>',views.book_api,name="bookapiint"),
                  path('login/', tview.obtain_auth_token,name="login"),
                  path('',include(router.urls)),
              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)