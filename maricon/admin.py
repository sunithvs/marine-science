from django.contrib import admin

from .models import CommitteeMember, Gallery, Speaker, Sponsor, Faq, Schedule, Committee, OTP

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
    list_display = ( 'otp', 'created_at')
