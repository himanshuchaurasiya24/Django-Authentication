








from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'blog', views.BlogModelViewSet, basename='Blog ModelViewSet')




urlpatterns = [
    path('', include(router.urls))    
]
