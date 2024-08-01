from django.shortcuts import render
from django.views import View
from blogs.models import Blog
from courses.models import Category


class BlogsPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        amount_of_categories = len(categories)

        context = {'blogs': blogs,
                   'categories': categories,
                   'amount_categories': amount_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog.html', context)


class Page(View):
    def get(self, request, slug):
        category = None
        print(slug)
        if slug == '/blog/single/None':
            category = Category.objects.get(slug=slug)
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'category': category,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog_detail.html', context)