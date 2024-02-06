from rest_framework import serializers
from .models import Shoe, Cleaning, ShoeAccessory

class ShoeAccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeAccessory
        fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
    # clean_for_today = serializers.SerializerMethodField()
    shoeAccessory = ShoeAccessorySerializer(many=True, read_only=True)

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
