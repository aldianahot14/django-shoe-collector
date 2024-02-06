from rest_framework import serializers
from .models import Shoe
from .models import Cleaning, ShoeAccessory

class ShoeSerializer(serializers.ModelSerializer):
    clean_for_today = serializers.SerializerMethodField()
    class Meta:
        model = Shoe
        fields = '__all__'
    
class CleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaning
        fields = '__all__'
        read_only_fields = ('shoe')

class ShoeAccessorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ShoeAccessory
    fields = '__all__'
