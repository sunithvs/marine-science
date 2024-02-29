import hashlib

from django.shortcuts import render
from django.views.generic import TemplateView

from config.settings import PAYMENT_KEY


# Create your views here.

def generate_token(consumer_data, salt):
    # Concatenate input values with pipe separator
    data_to_hash = "|".join(str(value) for value in consumer_data) + "|" + salt

    # Choose the hashing algorithm based on the request
    hashing_algorithm = hashlib.sha512
    print(data_to_hash)

    # Hash the data using the selected algorithm
    hashed_data = hashing_algorithm(data_to_hash.encode()).hexdigest()

    return hashed_data


class PaymentView(TemplateView):
    template_name = "payment/payment.html"

    def get(self, request, *args, **kwargs):
        consumer_data = {
            'merchant_id': 'T1002122',
            'txn_id': 'dn5qux',
            'total_amount': '1',
            'account_no': '',
            'consumer_id': '',
            'consumer_mobile_no': '',
            'consumer_email_id': '',
            'debit_start_date': '',
            'debit_end_date': '',
            'max_amount': '',
            'amount_type': '',
            'frequency': '',
            'card_number': '',
            'exp_month': '',
            'exp_year': '',
            'cvv_code': '',
        }

        salt = PAYMENT_KEY

        generated_token = generate_token(list(consumer_data.values()), salt)
        print(generated_token)
        return render(request, self.template_name, {'token': generated_token, 'consumer_data': consumer_data})
