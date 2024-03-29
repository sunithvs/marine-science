import csv
import os
import zipfile
from io import BytesIO

from django.contrib import admin, messages
from django.http import HttpResponse

from .models import CommitteeMember, Gallery, Speaker, Sponsor, Faq, Schedule, Committee, OTP, PaperAbstract

admin.site.register(CommitteeMember)
admin.site.register(Gallery)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Faq)
admin.site.register(Schedule)


@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('otp', 'created_at')


@admin.register(PaperAbstract)
class PaperAbstractAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'created_at','presentation')
    search_fields = ('title', 'authors')
    list_filter = ('created_at', 'theme','presentation')
    actions = ['export_as_csv','download_as_zip']

    def export_as_csv(self, request, queryset):
        try:
            meta = self.model._meta

            field_names = ['title', 'authors', 'abstract', 'keywords',
                           'created_at',
                           'theme', 'presentation', 'file']

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
            writer = csv.writer(response)

            writer.writerow(field_names)
            for obj in queryset:
                 writer.writerow([getattr(obj, field) for field in field_names])
            return response
        except Exception as e:
            messages.error(request, "Error in exporting CSV")

    def download_as_zip(self, request, queryset):
        # Create a BytesIO object to hold the ZIP file
        filter_values = request.GET
        zip_buffer = BytesIO()
        filters_applied = '_'.join([f"{key}-{value}" for key, value in filter_values.items()])


        # Create a ZIP file in memory
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for obj in queryset:
                file_path = obj.file.path
                file_name = os.path.basename(file_path)
                # Make sure the file exists before adding it
                if os.path.isfile(file_path):
                    zip_file.write(file_path, file_name)

        # Rewind the buffer
        zip_buffer.seek(0)
        file_name_suffix = filters_applied if filters_applied else 'myfiles'

        # Construct the HTTP response
        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={file_name_suffix}.zip'

        return response

    def has_delete_permission(self, request, obj=None):
        return False

