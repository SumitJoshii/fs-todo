from rest_framework import serializers
from .models import User, List, MyTask

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]


class UserReadOnlySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

    

class ListSerializer(serializers.ModelSerializer):
    user = UserReadOnlySerializer(required=False, read_only=True)#????
    user_id = serializers.IntegerField(required = False)
    class Meta:
        model = List
        fields = [
            'id',
            'user',
            'user_id',
            'list_name',
            'is_important',
        ]



    # def create(self, validated_data):
    #     print("Validated Date 1: ", validated_data)
    #     #jaadoo tona ++
    #     #Method 1
    #     # user = User.objects.get(id = validated_data['user']['id'])
    #     # validated_data.pop('user')

    #     #Method 2
    #     # validated_data['user_id'] = validated_data['user']['id']
    #     # validated_data.pop('user')

    #     instance = super().create(validated_data)
    #     # instance.user = user
    #     # instance.save()
    #     print("Validated Date 2: ", validated_data)
    #     print("Instance: ",instance)
    #     return validated_data

class ListReadOnlySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    list_name = serializers.CharField(required = False)
    
    class Meta:
        model = List
        fields = [
            'id',
            'list_name',
        ]

class MyTaskReadOnlySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    class Meta:
        model = MyTask
        fields = [
            'id',
            'title',
            'description',
        ]

class MyTaskSerializer(serializers.ModelSerializer):
    list = ListReadOnlySerializer(required = False, read_only=True)
    list_id = serializers.IntegerField(required = False)
    class Meta:
        model = MyTask
        # fields = "__all__"
        fields = [
            'id',
            'list',
            'list_id',
            'title',
            'description',
            'is_complete',
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

class ExpandListSerializer(serializers.ModelSerializer):
    user = UserReadOnlySerializer(required=False)#????
    mytask_set = MyTaskReadOnlySerializer(many = True, read_only = True)
    class Meta:
        model = List
        fields = [
            'id',
            'user',
            'mytask_set',
            'list_name',
        ]
