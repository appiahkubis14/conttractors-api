from rest_framework import serializers
from .models import Contractor, Farmer
from rest_framework import serializers
from .models import Contractor
from django.contrib.auth.models import Group, Permission

class ContractorSerializer(serializers.ModelSerializer):
    # If you want to allow group and permissions during registration, you can serialize them like this
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False)
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True, required=False)

    class Meta:
        model = Contractor
        fields = ['username', 'password', 'full_name', 'groups', 'user_permissions']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Check if 'groups' and 'user_permissions' are part of validated_data
        groups = validated_data.pop('groups', [])
        user_permissions = validated_data.pop('user_permissions', [])
        
        # Create user
        user = Contractor.objects.create_user(**validated_data)

        # Add groups and permissions
        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)

        return user


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'
