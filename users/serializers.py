from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = get_user_model().objects.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return user
    