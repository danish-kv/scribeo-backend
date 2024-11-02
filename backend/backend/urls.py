from django.contrib import admin
from django.urls import path, include
from blog.views import PostViewSet
from users.views import CustomTokenObtainPairView, RegisterAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(f"posts", PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/register/', RegisterAPIView.as_view(), name='register')
    
]
