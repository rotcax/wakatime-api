# from rest_framework.response import Response
from rest.imports import Response, APIException, ParseError

class Util:
    def apiResponse(self, result, status = 200, message = ''):
        return Response({
            'result': result,
            'detail': message
        }, status=status)

    def throw404(self, message):
        raise ParseError(message)