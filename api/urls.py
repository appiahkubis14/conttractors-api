from django.urls import path
from .views import LoginView, RegisterContractorView, ContractorDetailView, RegisterFarmerView, FarmerDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    
    # Contractor CRUD endpoints
    path('contractors/', RegisterContractorView.as_view(), name='register_contractor'),
    path('contractors/<int:pk>/', ContractorDetailView.as_view(), name='contractor_detail'),

    # Farmer CRUD endpoints
    path('farmers/', RegisterFarmerView.as_view(), name='register_farmer'),
    path('farmers/<int:pk>/', FarmerDetailView.as_view(), name='farmer_detail'),
]
