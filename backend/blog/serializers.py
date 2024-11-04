from rest_framework import serializers
from .models import Post, Category
from users.models import CustomUser




class UserSerializer(serializers.ModelSerializer):
    my_blogs = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'my_blogs', 'profile', 'bio']

    def get_my_blogs(self, obj):
        posts = obj.posts.all()  
        return PostSerializer(posts, many=True).data 
    
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile', 'bio']




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  
    category_data = serializers.SerializerMethodField()  
    
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['user']

    def get_category_data(self, obj):
        return CategorySerializer(obj.category).data if obj.category else None
   


