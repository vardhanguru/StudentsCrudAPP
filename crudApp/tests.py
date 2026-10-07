from django.test import SimpleTestCase
from django.urls import resolve

from crudApp.views import (
    DeleteStudentView,
    StudentCreateView,
    StudentDetailsView,
    StudentListView,
    StudentUpdateView,
)


class StudentClassBasedViewTests(SimpleTestCase):
    def test_student_list_route_uses_class_based_view(self):
        self.assertEqual(resolve('/students/').func.view_class, StudentListView)

    def test_student_create_route_uses_class_based_view(self):
        self.assertEqual(resolve('/students/add/').func.view_class, StudentCreateView)

    def test_student_update_route_uses_class_based_view(self):
        self.assertEqual(resolve('/students/update/1/').func.view_class, StudentUpdateView)

    def test_student_delete_route_uses_class_based_view(self):
        self.assertEqual(resolve('/students/delete/1/').func.view_class, DeleteStudentView)

    def test_student_detail_route_uses_class_based_view(self):
        self.assertEqual(resolve('/students/1/').func.view_class, StudentDetailsView)
