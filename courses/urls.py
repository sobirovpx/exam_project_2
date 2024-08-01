from django.urls import path

from courses.views.views import IndexPage, CoursePage, ContactPage, AboutPage, BasePage, CourseDetailPage, CCatDetailPage
from courses.views.authentication import SignUpView

urlpatterns = [
    # index
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursePage.as_view(), name='course'),
    path('', BasePage.as_view(), name='base'),
    path('course/<slug:slug>/', CourseDetailPage.as_view(), name='c_detail'),
    path('category/<slug:slug>/', CCatDetailPage.as_view(), name='cg_detail'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),

    # auth
    path('auth/', SignUpView.as_view(), name='auth'),
]