from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify

from blogs.models import Author, Blog
from teachers.models import Teacher


class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(upload_to='images/categories', null=True, blank=True)

    class Meta:
        verbose_name = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.name)}-{i}"
                if not Category.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/courses', null=True, blank=True)
    video = models.FileField(upload_to='videos/courses')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.name)}-{i}"
                if not Course.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    is_published = models.BooleanField(default=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')


