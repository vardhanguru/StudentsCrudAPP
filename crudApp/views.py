from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from crudApp.forms import StudentForm
from crudApp.models import Student


# Create your views here.

def studentView(request):
    students = Student.objects.all()
    return render(request, 'studentList.html', {'students': students})


# Class Based View
class StudentListView(ListView):
    model = Student
    template_name = 'studentList.html'
    context_object_name = 'students'


def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    return render(request, 'studentForm.html', {'form': form})


# class based view for this
class StudentCreateView(CreateView):
    model = Student
    template_name = 'studentForm.html'
    fields = '__all__'
    success_url = '/students/'


def studentDelete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student-list')


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = '/students/'


def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-list')
    return render(request, 'studentUpdateForm.html', {'form': form})


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'studentUpdateForm.html'
    fields = '__all__'
    success_url = '/students/'


class StudentDetailsView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'