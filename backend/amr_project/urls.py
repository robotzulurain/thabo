from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('amr_api.urls')),
    path('', views.home, name='home'),  # Add this line for root URL
]
