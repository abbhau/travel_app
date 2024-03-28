from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    ''' Serializer for serialize the data of User and vice versa '''
    
    class Meta:
        model = User
        fields = ['id','username','password','email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)