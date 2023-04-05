from django.contrib import admin
from django.urls import path
from models import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('default/', views.default),
    path('backup/', views.backup),
]
