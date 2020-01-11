from rest.serializers.serializers import TimeTrackSerializer
from rest.imports import status, APIView, Util, serializers, ParseError
from rest.models.models import TimeTrack
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
                'date_coding': date,
                'start': request['start'],
                'end': request['end'],
                'timezone': request['timezone']
            }

            return self.apiResponse(self.__create_timetrack(date, timetrack), status.HTTP_201_CREATED)

        except:
            raise

    def __validate_field(self, apikey, date):
        try:
            if not(apikey):
                self.throw400('apikey is required')

            if not(date):
                self.throw400('date is required')

        except:
            raise

    def __validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')

        except ValueError:
            self.throw400('Incorrect date format, should be YYYY-MM-DD')

    def __fetch_wakatime(self, apikey, date):
        try:
            encoded_bytes = base64.b64encode(apikey.encode("utf-8"))
            encoded_str = str(encoded_bytes, "utf-8")

            params = { 'date': date }
            headers = { 'Authorization': 'Basic ' + encoded_str }
            req = requests.get('https://wakatime.com/api/v1/users/current/durations', params=params, headers=headers)

            req.raise_for_status()

            return req.json()

        except requests.exceptions.RequestException as e:
            self.throw400(e)

    def __create_timetrack(self, date, timetrack):
        try:
            exist_timetrack = TimeTrack.objects.get(date_coding=date)
            serializer = TimeTrackSerializer(exist_timetrack, data=timetrack)
            return self.__validate_serializer(serializer)

        except TimeTrack.DoesNotExist:
            serializer = TimeTrackSerializer(data=timetrack)
            return self.__validate_serializer(serializer)

    def __validate_serializer(self, serializer):
        try:
            if serializer.is_valid():
                serializer.save()
                return serializer.data

            self.throw400(serializer.errors)

        except:
            raise
