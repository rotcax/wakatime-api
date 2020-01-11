# from rest_framework.response import Response
from rest.imports import Response, APIException, ParseError
from pprint import pprint

class Util:
    def dump(self, instance):
        pprint(dir(instance))

    def apiResponse(self, result, status = 200):
        return Response({ 'result': result }, status=status)

    def throw400(self, message):
        raise ParseError({ 'error': message })

    def throw404(self, message):
        raise NotFound({ 'error': message })