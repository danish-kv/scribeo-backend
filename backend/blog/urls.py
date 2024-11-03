
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(f"posts", PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls))
]
