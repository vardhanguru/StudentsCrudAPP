from django.contrib import admin
from django.urls import path

from crudApp.views import (
    DeleteStudentView,
    StudentCreateView,
    StudentDetailsView,
    StudentListView,
    StudentUpdateView,
    createStudent,
    studentDelete,
    studentView,
    update,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/add/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailsView.as_view(), name='student-detail'),
    path('students/update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', DeleteStudentView.as_view(), name='student-delete'),

    # legacy function-based URLs kept for compatibility
    path('students/list/', studentView),
    path('add_student/', createStudent),
    path('delete_student/<int:id>', studentDelete),
    path('update/<int:id>', update),
]
