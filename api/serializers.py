from users.models import User
from lawyers.models import Lawyer
from landseller.models import LandSeller
from landbuyers.models import LandBuyer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MinimalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]

class MinimalLawyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = ["firm"]

class MinimalLandsellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandSeller
        fields = ["address"]


class MinimalLandBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandBuyer
        fields = ["address"]



class LawyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'


class LandsellersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandSeller
        fields = '__all__'

class LandBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandBuyer
        fields = '__all__'

   
   
   
   
   
   
   
   
   
   
   
   
    