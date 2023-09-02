from instances.serializers import UserSerializer
from instances.models import User
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
@api_view(['POST'])
def signup(request):
    """Allows user to signup

    Args:
        request (POST): Refer User Model

    Returns:
        HTTPS Status Code
    """
    serializer_class = UserSerializer(data = request.data)
    if serializer_class.is_valid():
        request.data.pop('retype_password', None)
        serializer_class.save()
        user = User.objects.get(username=request.data.get('username'))
        user.set_password(request.data.get('password'))
        user.save()
        token = Token.objects.create(user=user)

        return Response({'token' : token.key,
                         'username': user.username})
    
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """ Allows Users to login

    Args:
        request (POST): username : string
                        password : string

    Returns:
         HTTPS Status code
    """
    user = get_object_or_404(User, username=request.data.get('username'))

    if not user:
        return Response('User not fount', status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(request.data.get('password')):
        return Response('Invalid Credentials', status=status.HTTP_401_UNAUTHORIZED)
    
    token,is_created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key})