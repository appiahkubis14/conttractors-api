from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/contractor/', views.register_contractor, name='register_contractor'),
    path('register/farmer/', views.register_farmer, name='register_farmer'),
]
