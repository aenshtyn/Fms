from rest_framework import serializers
from .models import User, Farm, Invitation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number']

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

class FarmUsersSerializer(serializers.ModelSerializer):
    managers = UserSerializer(many=True)
    shareholders = UserSerializer(many=True)
    guests = UserSerializer(many=True)

    class Meta:
        model = Farm
        fields = ['id', 'name', 'managers', 'shareholders', 'guests']
