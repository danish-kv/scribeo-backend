
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CategoryViewSet, UserProfileViewSet, HomePageAPIView
from django.urls import path, include

router = DefaultRouter()
router.register(f"posts", PostViewSet, basename='posts')
router.register(f"category", CategoryViewSet, basename='category')
router.register(f"profile", UserProfileViewSet, basename='profile')

urlpatterns = [
    path("", include(router.urls)),
    path('homepage/', HomePageAPIView.as_view(), name='homepage')
]
