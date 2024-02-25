from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models

notice_types = [
    'Announcements',
    'Events',
    'News',
    'Other',
]


class Notice(models.Model):
    """
    Notice model
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    attachment = models.FileField(upload_to='notice/', blank=True, null=True)
    attachment_text = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    show_on_website = models.BooleanField(default=True)
    type = models.CharField(max_length=100, blank=True, null=True, choices=[
        (notice_type, notice_type) for notice_type in notice_types
    ])

    class Meta:
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title

    # validate if attachment is present then attachment_text is required and vice versa
    def clean(self):
        if self.attachment and not self.attachment_text:
            raise ValidationError('attachment_text is required')
        if self.attachment_text and not self.attachment:
            raise ValidationError('attachment is required')


class Gallery(models.Model):
    """
    gallery model
    """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)


class Seminar(models.Model):
    """
    Seminars model
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    link = models.URLField(blank=True, null=True)
    show_on_website = models.BooleanField(default=True)
    image = models.ImageField(upload_to='seminar/')

    def __str__(self):
        return self.title


class Facility(models.Model):
    """
    Facility model
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    link = models.URLField(blank=True, null=True)
    show_on_website = models.BooleanField(default=True)
    image = models.ImageField(upload_to='seminar/')

    def __str__(self):
        return self.title

    # meta
    class Meta:
        verbose_name_plural = "Facilities"


class Publication(models.Model):
    """
    Publication model
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    link = models.URLField(blank=True, null=True)
    show_on_website = models.BooleanField(default=True)
    image = models.ImageField(upload_to='seminar/')

    def __str__(self):
        return self.title


class Journals(models.Model):
    """
    Journals model
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    date = models.DateField(auto_now=True)
    link = models.URLField(blank=True, null=True)
    show_on_website = models.BooleanField(default=True)
    image = models.ImageField(upload_to='seminar/')

    def __str__(self):
        return self.title
