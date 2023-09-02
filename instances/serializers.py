from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, min_length=8, max_length=60)
    retype_password = serializers.CharField(required=True,write_only=True)

    class Meta:
        model = User
        fields = fields = ['name', 'email', 'username','password', 'retype_password',  'account_type']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('retype_password') :
            raise serializers.ValidationError('Passwords did not match')

        return attrs
