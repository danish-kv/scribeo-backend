from rest_framework import serializers
from .models import Post, Category
from users.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

        
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['user']
