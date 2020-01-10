from rest.serializers.serializers import TimeTrackSerializer
from rest.imports import status, APIView, Util, serializers, ParseError
import base64
import datetime
import requests

class TimeTrackList(APIView, Util):

    def post(self, request, format=None):
        try:
            data = request.data
            apikey = data.get('apikey')
            date = data.get('date')

            self.__validate_field(apikey, date)
            self.__validate_date(date)

            request = self.__fetch_wakatime(apikey, date)

            timetrack = {
                'created_at': '',
                'start': request['start'],
                'end': request['end'],
                'timezone': request['timezone']
            }

            ## Buscar en la base de datos si no hay un registro con la fecha de hoy, 
            # si es asi actualizar ese registro, se debe primero determinar que dia es hoy
            # y determinar que dia es el del created_at de la base de datos

            # serializer = TimeTrackSerializer(data=request.data)
            
            # if serializer.is_valid():
            #     serializer.save()
            #     return self.apiResponse(serializer.data, status.HTTP_201_CREATED)
                
            # return self.apiResponse({}, status.HTTP_400_BAD_REQUEST, serializer.errors)

            return self.apiResponse(timetrack, status.HTTP_201_CREATED)

        except:
            raise

    def __validate_field(self, apikey, date):
        try:
            if not(apikey):
                self.throw404('apikey is required')

            if not(date):
                self.throw404('date is required')

        except:
            raise

    def __validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')

        except ValueError:
            raise ParseError('Incorrect date format, should be YYYY-MM-DD')

    def __fetch_wakatime(self, apikey, date):
        encoded_bytes = base64.b64encode(apikey.encode("utf-8"))
        encoded_str = str(encoded_bytes, "utf-8")

        params = { 'date': date }
        headers = { 'Authorization': 'Basic ' + encoded_str }
        req = requests.get('https://wakatime.com/api/v1/users/current/durations', params=params, headers=headers)

        req.raise_for_status()

        return req.json()