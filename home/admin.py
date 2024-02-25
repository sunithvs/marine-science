from django.contrib import admin

from .models import Notice, Gallery, Seminar, Journals, Publication, Facility

admin.site.register(Notice)
admin.site.register(Gallery)
admin.site.register(Seminar)

admin.site.register(Journals)
admin.site.register(Publication)
admin.site.register(Facility)
