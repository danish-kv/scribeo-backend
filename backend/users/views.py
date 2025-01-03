from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.viewsets import ModelViewSet
from .serializers import RegisterSerializer, ProfileImageSerializer

user = get_user_model()

# Create your views here.


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)

        
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:

        try:
            res =  super().post(request, *args, **kwargs)
            print(res)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user
            print('=====',user.profile)
            profile_data = None
            if hasattr(user, 'profile') and user.profile:
                print('Profile image found')
                profile_serializer = ProfileImageSerializer(user)
                print('Profile serializer data:', profile_serializer.data)
                profile_data = profile_serializer.data.get('profile', None)


            res.data['user'] = user.username
            res.data['userID'] = user.id
            res.data['profile'] = profile_data
            print('last res ====', res)
            return res
        except Exception as e:
            print('exeption', e)
            return Response(data=str(e), status=status.HTTP_404_NOT_FOUND)
        



class Logout(APIView):
    def post(self, request):
        try:
            refresh = request.data.get('refresh')
            if not refresh:
                return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)

        except TokenError as e:
            return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


