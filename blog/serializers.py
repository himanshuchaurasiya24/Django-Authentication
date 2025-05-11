from .models import *
from rest_framework import serializers
from users.serializers import CustomUserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
    

        