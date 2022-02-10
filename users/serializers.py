from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        instance = User.objects.create_user(**validated_data)
        return instance