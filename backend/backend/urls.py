from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import PostViewSet
from users.views import CustomTokenObtainPairView, RegisterAPIView, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/logout/', Logout.as_view(), name='logout'),
    path("", include('blog.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
