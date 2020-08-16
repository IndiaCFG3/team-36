from django.contrib import admin
from .models import Keywords,Constraint,ScoresBatches,Attendance
# Register your models here.
admin.site.register(Keywords)
admin.site.register(Constraint)
admin.site.register(ScoresBatches)
admin.site.register(Attendance)
