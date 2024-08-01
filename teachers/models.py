from django.db import models
from django.utils.text import slugify


class Teacher(models.Model):
    class RatingChoices(models.TextChoices):
        Junior = 'Junior',
        Middle = 'Middle ',
        Senior = 'Senior'

    full_name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.CharField(max_length=55, choices=RatingChoices.choices, default=RatingChoices.Junior.value)
    twitter = models.CharField(max_length=150, null=True, blank=True)
    facebook = models.CharField(max_length=150, null=True, blank=True)
    linkedin = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='images/teachers', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)

        if self.slug:
            i = 1
            while True:
                new_slug = f"{slugify(self.full_name)}-{i}"
                if not Teacher.objects.filter(slug=new_slug).exists():
                    self.slug = new_slug
                    break
                i += 1

        super(Teacher, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
