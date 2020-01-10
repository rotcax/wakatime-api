from rest.serializers.serializers import UserSerializer
from rest.imports import status, APIView, Util, User

class UserList(APIView, Util):
    
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return self.apiResponse(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return self.apiResponse(serializer.data, status.HTTP_201_CREATED)
            
        return self.apiResponse({}, status.HTTP_400_BAD_REQUEST, serializer.errors)