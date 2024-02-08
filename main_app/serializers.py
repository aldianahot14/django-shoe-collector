from rest_framework import serializers
from .models import Shoe, Cleaning, ShoeAccessory
from django.contrib.auth.models import User

# include User serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class ShoeAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeAccessory
        fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
    # clean_for_today = serializers.SerializerMethodField()
    shoeAccessory = ShoeAccessorySerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shoe
        fields = '__all__'
    
class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'
        read_only_fields = ('shoe',)  # Add comma to make it a tuple


class ShoeAccessorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoeAccessory
    fields = '__all__'
