from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .models import Contractor, Farmer
from .serializers import ContractorSerializer, FarmerSerializer


@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    # Ensure that the username and password are provided in the request
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Authenticate the contractor using the authenticate function
    user = authenticate(username=username, password=password)
    
    # Check if the user exists and the credentials are correct
    if user and isinstance(user, Contractor):
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    
    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def register_contractor(request):
    serializer = ContractorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Contractor registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_farmer(request):
    serializer = FarmerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Farmer registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


