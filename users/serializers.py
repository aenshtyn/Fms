from rest_framework import serializers
from .models import  Farm, CustomUser, UserFarmRole

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        read_only_fields = ['role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role='Farm Owner'
        )
        return user

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

# class FarmUsersSerializer(serializers.ModelSerializer):
#     managers = UserSerializer(many=True)
#     shareholders = UserSerializer(many=True)
#     guests = CustomUserSerializer(many=True)

#     class Meta:
#         model = Farm
#         fields = ['id', 'name', 'managers', 'shareholders', 'guests']
