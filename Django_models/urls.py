from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.contrib import admin
from django.urls import path, include  # ← include функциясын кошобуз

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruits.urls')),  # ← fruits деген app'ке багыттайбыз
]
touch fruits/urls.py
