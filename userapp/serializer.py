from rest_framework import serializers
from userapp.models import Person,Peoples
from django.contrib.auth.models import User


#jwt based
class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)


    class Meta:
        model=User
        fields=['id','username','password','email']


    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user   


#signals used 
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Peoples
        fields='__all__'





#token based

class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self,data):
        if data["username"]:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username exists')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email already exists')
        return data
    
    def create(self,validated_data):
        obj1=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        obj1.set_password(validated_data['password'])
        obj1.save()
        return validated_data



class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()










# class PersonSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Person
#         fields ='__all__'