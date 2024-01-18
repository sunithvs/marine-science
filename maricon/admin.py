from django.contrib import admin

from .models import CommitteeMember, Gallery, Speaker, Sponsor, Faq, Schedule, Committee

admin.site.register(CommitteeMember)
admin.site.register(Gallery)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Faq)
admin.site.register(Schedule)

@admin.register(Committee)
class CommitteeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

