from django.urls import path, include

from rest_framework.routers import DefaultRouter

from employee_meetings_api import views


router = DefaultRouter()
# router.register('profile', views.EmployeeProfileViewSet)
router.register('employee_profile', views.EmployeeProfileViewSet)
router.register('reservation', views.ReservationViewSet)
router.register('meetingroom', views.MeetingRoomViewSet)

urlpatterns = [
    path('login/', views.EmployeeLoginApiView.as_view()),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
