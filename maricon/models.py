from django.db import models


# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='speakers', null=True, blank=True)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    google_scholar = models.URLField(max_length=100, null=True, blank=True)
    linkedin = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sponsors', null=True, blank=True)
    website = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    day = models.CharField(max_length=100, choices=(('Day 1', 'Day 1'), ('Day 2', 'Day 2'), ('Day 3', 'Day 3')))

    class Meta:
        ordering = ['date', 'time']
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return self.title


class Committee(models.Model):
    SIZE_CHOICES = [
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
    ]

    name = models.CharField(max_length=100)
    size_on_website = models.IntegerField(choices=SIZE_CHOICES)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['size_on_website']

    def __str__(self):
        return self.name


class CommitteeMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='committee', null=True, blank=True)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    facebook = models.URLField(max_length=100, null=True, blank=True)
    twitter = models.URLField(max_length=100, null=True, blank=True)
    google_scholar = models.URLField(max_length=100, null=True, blank=True)
    linkedin = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery', null=True, blank=True)

    def __str__(self):
        return self.image.name


class Theme(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
