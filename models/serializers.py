from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    retype_password = serializers.CharField(required=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('retype_password') :
            raise serializers.ValidationError('Passwords did not match')
        
        return attrs
