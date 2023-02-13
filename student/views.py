from django.shortcuts import render
from django.http import HttpResponse
from student.models import student_details
# Create your views here.
def home(Request):
    return render(Request,'student_reg/home.html')
#   return HttpResponse("This is my Home page")


def reg(Request):
    return render(Request, 'student_reg/reg.html')
#    return HttpResponse("This is my Registration page")

def report(Request):
    student_mdl_details = student_details.objects.order_by("id")
    student_details_dict = {'insert_student_details': student_mdl_details }
    return render(Request,"student_reg/report.html", context=student_details_dict)
    #return HttpResponse("This is my Report page")