from rest_framework import viewsets, permissions, status
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, UserSerializer
from users.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'


    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(user=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    



class HomePageAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        total_blogs = Post.objects.count()  
        total_users = CustomUser.objects.count() 

        data = { 
            'total_blogs': total_blogs, 
            'total_users': total_users 
        }
        return Response(data=data, status=status.HTTP_200_OK)
