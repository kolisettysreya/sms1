from django.shortcuts import render
from django.contrib.auth.models import User
from facultyapp.models import Marks
from adminapp.models import StudentList


# Create your views here.
#def projecstudentpage(request):
  # return render(request,'ProjectStudentPage.html')
def studenthomepage(request):
    return render(request,'studentapp/StudentHomePage.html')
def view_marks(request):
    user=request.user
    try:
        student_user=User.objects.get(username=user.username)
        student=StudentList.objects.get(Register_Number=student_user)
        marks=Marks.objects.filter(student=student)
        return render(request,'studentapp/view-marks.html',{'marks':marks})
    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request, 'studentapp/no_studentList.html',{'error':'No student record found for this user.'})

