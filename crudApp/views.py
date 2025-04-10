from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

# Create your views here.

def studentView(request):
    students = Student.objects.all()
    return render(request, 'studentList.html', {'students': students})


def createStudent(request):
    form = StudentForm(request.POST)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(studentView)
    return render(request, 'studentForm.html', {'form': form})


def studentDelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(studentView)

def update(request,id):
    student = Student.objects.get(id=id)
    format = StudentForm(instance=student)
    if request.method == 'POST':
        format = StudentForm(request.POST,instance=student)
        if format.is_valid():
            format.save()
            return redirect(studentView)
    return render(request, 'studentUpdateForm.html', {'form': format})





