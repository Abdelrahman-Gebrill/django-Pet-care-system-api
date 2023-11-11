from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['id']
        write_only_fields = ['password']
        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128,min_length=6,write_only=True)
    email = serializers.EmailField(max_length = 150,min_length=11)
    class Meta:
        model = User
        fields = ['id','email','firstname','lastname','password','tokens']
        read_only_fields = ['id','firstname','lastname','tokens']
    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        user = auth.authenticate(email = email,password = password)
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        return {
            'id':user.id,
            'email':user.email,
            'firstname':user.firstname,
            'lastname':user.lastname,
            'tokens':user.tokens,
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Invalid or expired token')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError as te:
            self.fail('bad_token')