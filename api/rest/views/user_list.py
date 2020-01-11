from rest.serializers.serializers import UserSerializer
from rest.imports import status, APIView, Util, User

class UserList(APIView, Util):
    def get(self, request, format=None):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return self.apiResponse(serializer.data)

        except:
            raise

    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                return self.apiResponse(serializer.data, status.HTTP_201_CREATED)
                
            self.throw400(serializer.errors)
        
        except:
            raise