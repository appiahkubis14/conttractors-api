from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404
from django.contrib.auth import authenticate
from .models import Contractor, Farmer
from .serializers import ContractorSerializer, FarmerSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user:
            if isinstance(user, Contractor):
                return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User is not a contractor"}, status=status.HTTP_403_FORBIDDEN)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)




class RegisterContractorView(APIView):
    def post(self, request):
        serializer = ContractorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contractor registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ContractorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

    def get(self, request, pk):
        contractor = get_object_or_404(Contractor, pk=pk)
        serializer = self.serializer_class(contractor)
        return Response(serializer.data)

    def put(self, request, pk):
        contractor = get_object_or_404(Contractor, pk=pk)
        serializer = self.serializer_class(contractor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contractor updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contractor = get_object_or_404(Contractor, pk=pk)
        contractor.delete()
        return Response({"message": "Contractor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class RegisterFarmerView(APIView):
    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Farmer registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FarmerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def get(self, request, pk):
        farmer = get_object_or_404(Farmer, pk=pk)
        serializer = self.serializer_class(farmer)
        return Response(serializer.data)

    def put(self, request, pk):
        farmer = get_object_or_404(Farmer, pk=pk)
        serializer = self.serializer_class(farmer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Farmer updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        farmer = get_object_or_404(Farmer, pk=pk)
        farmer.delete()
        return Response({"message": "Farmer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
