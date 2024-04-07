from django.contrib import admin

# Register your models here.
from .models import Employee, Task, Leave, Department, Onboarding, Position, Recruitment, Feedback, Attendance

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Leave)
admin.site.register(Onboarding)
admin.site.register(Recruitment)
admin.site.register(Feedback)
admin.site.register(Attendance)