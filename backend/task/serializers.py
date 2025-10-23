from rest_framework import serializers
from .models import Task, CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Task
        fields = ['id', 'title','owner', 'description', 'completed', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required =True, validators=[validate_password])
    phone = serializers.CharField(required=False, allow_blank=True)

    class Meta:
      model = User
      fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone' ] 

    def create(self, validated_data):
      return User.objects.create_user(**validated_data)