from django.shortcuts import render
# I Combine all Repeated Response and status code in one file ('Don't Repeat Your Self')
from Common_Responses import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .serializers import LoginSerializer, LogoutSerializer, UserSerializers

@authentication_classes([])
@permission_classes([])
# Create your views here.
@api_view(['GET','POST'])
def Registration(request):  
    
    if request.method=='GET':
        try:
            users = User.objects.all()
        except:
            return Bad_Response(data=None,From='GET Registration User')
        serializers = UserSerializers(instance=users,many=True)
        return Ok_Response(serializers.data)
    
    elif request.method=='POST':
        serializers = UserSerializers(data=request.data)
        if serializers.is_valid():
            instance =serializers.save()
            instance.set_password(instance.password)
            instance.save()
            return Created_Response()
        else:
            return Bad_Response(data=serializers.errors,From=None)
    else:
        return Bad_Response(data=None,From='ALL Regestration User')


@api_view(['GET','PUT','DELETE'])
def Mentainanace(request,pk):
    try:
        user = User.objects.get(id=pk)
    except:
        return Bad_Response(data=None,From='Try Mentainance of User')
    if request.method == 'PUT':
        deserializer = UserSerializers(instance=user,data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return No_Content_Response()
        else:
            return Bad_Response(data=deserializer.errors,From='PUT Mentainance User')
    elif request.method == 'GET':
        serializers = UserSerializers(instance=user)
        return Ok_Response(data=serializers.data)
    elif request.method == 'DELETE':
        user.delete()
        return No_Content_Response()
    else:
        return Bad_Response(data=None,From='ALL Mentainance User')

@authentication_classes([])
@permission_classes([])
def Login(request):
        serializers = LoginSerializer(data=request.data)
        if serializers.is_valid():
            return Ok_Response(serializers.data)
        else:
            return Unautherized_Response(serializers.errors)


def Logout(request):
    serializers = LogoutSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return No_Content_Response()
    else:
        return Unautherized_Response(serializers.errors)
