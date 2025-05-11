from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Prevent exposure in responses

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'bio', 'profile_picture', 'facebook', 'youtube', 'instagram', 'twitter']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Handles user registration and ensures password security."""
        user = CustomUser.objects.create_user(**validated_data)
        # user = get_user_model().objects.create_user(
        #     username=validated_data['username'],
        #     email=validated_data['email'],
        #     # first_name=validated_data.get('first_name',''), # if you dont want the first name required 
        #     first_name=validated_data.get('first_name',''),
        #     last_name=validated_data.get('last_name'),
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        return user

    def update(self, instance, validated_data):
        """Ensure password updates are handled securely, but not required."""
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))  # Secure password update

        for key, value in validated_data.items():
            setattr(instance, key, value)  # Dynamically update other fields

        instance.save()
        return instance

