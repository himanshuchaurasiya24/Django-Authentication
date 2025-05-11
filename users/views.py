from users.models import CustomUser
from users.serializers import *
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from users.serializers import CustomUserSerializer
from rest_framework.permissions import *
from rest_framework import permissions 

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Allow read-only access
            return True
        return obj.id == request.user.id  # Ensure users can only modify their own profile

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    def get_queryset(self):
        """Ensure users can only see and edit their own profile."""
        if self.request.user.is_authenticated:
            return CustomUser.objects.filter(id=self.request.user.id)  # Only return logged-in user's data
        return CustomUser.objects.none()  # Block unauthorized access

    def get_permissions(self):
        """Allow anyone to register, restrict other actions."""
        if self.action == 'create':  # Allow registration without authentication
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]


    def perform_create(self, serializer):
        """Handles user registration securely."""
        serializer.save()

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return CustomUser.objects.filter(id=self.request.user.id)  # Only return the logged-in user's data
    #     return CustomUser.objects.none() 






'''
 to get different serializers based on action in viewset
def get_serializer_class(self):
        """Use different serializers based on action."""
        if self.action in ['update', 'partial_update']:
            return CustomUserProfileSerializer
        return CustomUserSerializer

'''
# @api_view(['POST', 'GET'])
# def register_user(request):
#     serializer = CustomUserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User registered successfully","details":serializer.data}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['PUT', 'PATCH'])
# def update_user_profile(request):
#     user = request.user
#     serializers = CustomUserProfileSerializer(user, data=request.data, partial=True)
#     if serializers.is_valid():
#         serializers.save()
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
