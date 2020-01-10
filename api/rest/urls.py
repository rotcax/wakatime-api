from django.urls import include, path
from rest.views.views import api_root, UserList, UserDetail, TimeTrackList

urlpatterns = [
    path('', api_root),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-list'),
    path('timetracks/', TimeTrackList.as_view(), name='timetrack')
]
