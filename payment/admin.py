from django.contrib import admin

from payment.models import Payment


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
	fields = ['id', 'amount', 'currency', 'user', 'status', 'category']
	list_display = ['id', 'amount', 'currency', 'user', 'status', 'category']
	list_filter = ['status', 'category']
	search_fields = ['id', 'user__email', 'user__full_name', ]
	readonly_fields = ['id']

	actions = ['export_as_csv']

	def export_as_csv(self, request, queryset):
		import csv
		from django.http import HttpResponse
		from django.utils.encoding import smart_str
		import datetime

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename=payment-{}.csv'.format(datetime.datetime.now())

		writer = csv.writer(response)
		writer.writerow(['User name', 'User Email', 'User Phone', 'Amount', 'Currency', 'Status', 'Category'])
		for obj in queryset:
			writer.writerow(
				[smart_str(obj.user.full_name), smart_str(obj.user.email), smart_str(obj.user.mobile_number),
				 smart_str(obj.id), smart_str(obj.amount), smart_str(obj.currency), smart_str(obj.user),
				 smart_str(obj.status), smart_str(obj.category)])
		return response
