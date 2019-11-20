from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from employee_meetings_api import views

schema_view = get_swagger_view(title='Employee Meeting API')

router = DefaultRouter()

urlpatterns = [
    url(r'^meetingroom-list/$',
        views.MeetingRoomList.as_view(),
        name=views.MeetingRoomList.name),
    url(r'^meetingroom-list/(?P<pk>[0-9]+)$',
        views.MeetingRoomDetail.as_view(),
        name=views.MeetingRoomDetail.name),
    url(r'^rooms/$',
        views.RoomList.as_view(),
        name=views.RoomList.name),
    url(r'^rooms/(?P<pk>[0-9]+)$',
        views.RoomDetail.as_view(),
        name=views.RoomDetail.name),
    url(r'^employee_profiles/$',
        views.EmployeeProfileList.as_view(),
        name=views.EmployeeProfileList.name),
    url(r'^employee_profiles/(?P<pk>[0-9]+)$',
        views.EmployeeProfileDetail.as_view(),
        name=views.EmployeeProfileDetail.name),
    url(r'^reservations/$',
        views.ReservationList.as_view(),
        name=views.ReservationList.name),
    url(r'^reservations/(?P<pk>[0-9]+)$',
        views.ReservationDetail.as_view(),
        name=views.ReservationDetail.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    path('login/', views.EmployeeLoginApiView.as_view()),
    path(r'swagger-docs/', schema_view),
]
