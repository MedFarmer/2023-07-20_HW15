from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse

def index(request):    
    students = Student.objects.all()
    fnames = [student.fname for student in students]
    lnames = [student.lname for student in students]
    gpas = [student.gpa for student in students]
    context = {'fnames':fnames,'lnames':lnames, 'gpas':gpas }  
    return JsonResponse(context)

def add_student(request):
    if request.method == 'POST':
        students = request.POST
        fname = students['fname']
        lname = students['lname']
        gpa = students['gpa']
        add = Student()
        add.fname = fname
        add.lname = lname
        add.gpa = gpa
        add.save()
        return redirect('index')        
    else:
        return render(request, 'add_student.html')