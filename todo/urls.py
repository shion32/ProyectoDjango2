from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home,name="home"),
    path("agregar/", views.agregar, name="agregar"),
]
