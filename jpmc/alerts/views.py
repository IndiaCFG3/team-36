from django.shortcuts import render
from .models import Keywords,Constraint,ScoresBatches,Attendance
# Create your views here.

def sendnotif(request):
    #basically check for attendance and marks
    return render(request, 'dashboard.html')

def shownotif(request):
    notification = dict()
    if (request.user.is_authenticated):
        attendence = Attendance.objects.filter(student_id = request.user)
        performance = ScoresBatches.objects.filter(student_id = request.user)
        # for i in Constraint.objects.all():
        #     #alert = Keywords("short attendence",True)
        #     #alert = Keywords.objects.filter(i.alert_id) 
        #     alert = i.alert_id
        #     print(alert)
        #     if alert.is_attendance:
        #         attendence_percentage = (attendance.total_lectures - attendence.attendance)*100/attendance.total_lectures
        #         if(alert.threshold_min > attendence_percentage and attendence_percentage < alert.threshold_max):
        #             notification['attendence'] = alert.alert_message
        #     else:
        #         score = performance.score
        #         if(alert.threshold_min > score and score < alert.threshold_max):
        #             notification['score'] = alert.alert_message
    return render(request, 'notification.html', notification)
    