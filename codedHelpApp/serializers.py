from rest_framework import serializers
from .models import projectModel, requestModel


class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = ['id', 'title', 'created_on',
                  'max_number', 'estimate_time', 'coder']


class projectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = ['title', 'created_on',
                  'max_number', 'estimate_time', 'coder', 'detail']


class projectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = ['title', 'detail',
                  'max_number', 'estimate_time', ]


class requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['id', 'coder_profile', 'project']


class requestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['coder_profile', 'project', 'message']


class requestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['message', 'project', ]


class UserLoginSerializer(serializers.Serializer):

    def validate(self, data):
        my_username = data.get('username')
        my_password = data.get('password')

        try:
            user_obj = User.objects.get(username=my_username)
        except:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError(
                "Incorrect username/password combination! Noob..")

        return data
