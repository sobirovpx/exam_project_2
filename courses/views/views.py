from django.shortcuts import render
from django.views import View
from blogs.models import Blog
from courses.models import Course, Category, Comment
from teachers.models import Teacher


class BasePage(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories, }

        return render(request, 'base.html', context)

class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        blogs = Blog.objects.all()

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'blogs': blogs,
                   'active_page': 'home'}

        return render(request, 'courses/index.html', context)


class CoursePage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course,
                   'active_page': 'courses'}

        return render(request, 'courses/course.html', context)


class CourseDetailPage(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        comments = Comment.objects.filter(course_id__slug=slug)
        categories = Category.objects.all()
        blogs = Blog.objects.all()

        context = {'course': course,
                   'comments': comments,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'courses/course_detail.html', context)


class CCatDetailPage(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        categories = Category.objects.all()
        blogs = Blog.objects.all()

        context = {'category': category,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'courses/category_detail.html', context)


class ContactPage(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {'categories': categories,
                   'active_page': 'contact'}

        return render(request, 'info/contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.all()
        categories = Category.objects.all()

        context = {'comments': comments,
                   'categories': categories,
                   'active_page': 'about'}

        return render(request, 'info/about.html', context)