from rest_framework import serializers
from .models import projectModel, requestModel, User


class projectSerializer(serializers.ModelSerializer):
    coder = serializers.SlugRelatedField(

        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = projectModel
        fields = ['id', 'title', 'created_on',
                  'max_number', 'estimate_time', 'coder', 'detail']


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

    coder_profile = serializers.SlugRelatedField(

        read_only=True,
        slug_field='username'
    )

    project = serializers.SlugRelatedField(

        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = requestModel
        fields = ['id', 'coder_profile', 'project', 'message', 'status']


class requestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['coder_profile', 'project', 'message']


class requestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['message', 'project', ]


class requestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = requestModel
        fields = ['status']


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


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", ]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        #
        # payload = jwt_payload_handler(new_user)
        # token = jwt_encode_handler(payload)
        #
        # validated_data["token"] = token
        return validated_data
