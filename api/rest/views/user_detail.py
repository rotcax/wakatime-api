from rest.serializers.serializers import UserSerializer
from rest.imports import status, APIView, Util, User, Http404

class UserDetail(APIView, Util):
    def get(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return self.apiResponse(serializer.data)

        except:
            raise

    def put(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return self.apiResponse(serializer.data)

            self.throw400(serializer.errors)
        
        except:
            raise

    def delete(self, request, pk, format=None):
        try:
            user = self.get_object(pk)
            user.delete()
            return self.apiResponse({}, status.HTTP_204_NO_CONTENT)

        except:
            raise

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
            
        except User.DoesNotExist:
            self.throw404('user not found')