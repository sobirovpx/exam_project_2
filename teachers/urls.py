from django.urls import path
from teachers.views import TeacherPage, TeacherDetail

urlpatterns = [
    path('', TeacherPage.as_view(), name='teacher'),
    path('teachers/<slug:slug>', TeacherDetail.as_view(), name='slug'),
]