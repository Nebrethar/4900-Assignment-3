from rest_framework import serializers
from .models import Movie, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def create(self, validated_data):
        print("VALIDATED DATA")
        print(validated_data)
        customuser = CustomUser.objects.create_user(
            validated_data['username'],
            customusername = validated_data['customusername'],
            password = validated_data['password'],
            phone = validated_data['phone'],
            address = validated_data['address'],
            city = validated_data['city'],
            country = validated_data['country']
        )
        return customuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
class MovieSerializer(serializers.ModelSerializer):
 
    class Meta:
            model = Movie
            fields = ('pk','name', 'description', 'year', 'rating')

