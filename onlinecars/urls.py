"""
URL configuration for onlinecars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("cars/", cars, name='all_cars'),
    path('car-details/<int:pk>', get_by_id),
    path('', register),
    path('login/', user_login, name="login"),
    path('logout/', logout_view),
    path('add-car/', ImageCreateView.as_view()),
    path('add-comment/', add_comment, name='add-comment'),
    path('search/', search, name='search'),
    path('brands/<int:pk>',brands)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
