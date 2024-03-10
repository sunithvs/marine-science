from django.contrib import admin

from payment.models import Payment


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fields = ['id', 'amount', 'currency', 'user', 'status', 'category']
    list_display = ['id', 'amount', 'currency', 'user', 'status', 'category']
    list_filter = ['status', 'category']
    search_fields = ['id', 'user__username']
    readonly_fields = ['id']

