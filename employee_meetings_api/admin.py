from django.contrib import admin

from employee_meetings_api import models


admin.site.register(models.EmployeeProfile)
admin.site.register(models.Reservation)
# admin.site.register(models.MeetingRoom)
