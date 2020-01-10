from rest.imports import api_view, Response, reverse

from rest.views.user_list import UserList
from rest.views.user_detail import UserDetail
from rest.views.timetrack_list import TimeTrackList

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'timetracks': reverse('timetrack', request=request, format=format),
    })
