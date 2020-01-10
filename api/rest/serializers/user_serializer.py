from rest.imports import serializers, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user