from rest_framework import serializers
from .models import Brand  # Adjust import based on your project structure

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'  # Or specify the fields you want to include
