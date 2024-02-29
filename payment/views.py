import hashlib
from hmac import compare_digest

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from config.settings import PAYMENT_KEY
from .models import Payment

amount_dict = {
    'id': {
        'amount': '300',
        'currency': 'USD',
        'late_fee': '350',
    }, 'is': {
        'amount': '150',
        'currency': 'USD',
        'late_fee': '175',
    }, 'nd': {
        'amount': '3000',
        'currency': 'INR',
        'late_fee': '3500',

    }, 'rs': {
        'amount': '1500',
        'currency': 'INR',
        'late_fee': '1750',
    },
    'sp': {
        'amount': '600',
        'currency': 'INR',
        'late_fee': '750',
    },

}


def verify_payment(data, token):
    generated_token = generate_token_from_dict(data, PAYMENT_KEY)
    return compare_digest(generated_token, token)


def hash_str(data):
    # Choose the hashing algorithm based on the request
    hashing_algorithm = hashlib.sha512
    print(f"{data=}")

    # Hash the data using the selected algorithm
    hashed_data = hashing_algorithm(data.encode()).hexdigest()
    return hashed_data


def generate_token_from_dict(consumer_data, salt):
    # Concatenate input values with pipe separator
    data_to_hash = "|".join(str(value) for value in consumer_data) + "|" + salt

    return hash_str(data_to_hash)


class PaymentView(TemplateView):
    template_name = "payment/checkout.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, {})
        else:
            return redirect('/maricon/login/?next=/maricon/payment/')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("authenticated", request.POST['category'], amount_dict[request.POST['category']]['amount'])

            payment = Payment.objects.create(
                amount=amount_dict[request.POST['category']]['amount'],
                currency=amount_dict[request.POST['category']]['currency'],
                user=request.user
            )
            print("payment", payment)
            consumer_data = {
                'merchant_id': 'T1002122',
                'txn_id': payment.id,
                'total_amount': '1',  # TODO: change this to payment.amount
                'account_no': '',
                'consumer_id': '',
                'consumer_mobile_no': '',
                'consumer_email_id':'',
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

            generated_token = generate_token_from_dict(list(consumer_data.values()), salt)
            print(generated_token)
            return render(request, "payment/payment.html", {'token': generated_token, 'consumer_data': consumer_data})
        else:
            print("koooooi")
            return redirect('/maricon/login/?next=/maricon/payment/')


@csrf_exempt
def payment_verification(request):
    # Extract necessary information from the request
    payment_data = request.POST
    t_data = payment_data["msg"].split("|")
    txn_id = t_data[3]
    token = t_data.pop()
    val = 0
    if verify_payment(t_data, token):
        payment = Payment.objects.filter(id=txn_id)
        if not payment.exists():
            return JsonResponse({'status': 'failure'})
        payment = payment.first()
        if t_data[1] == 'success':
            payment.status = 'success'
            payment.save()
        else:
            payment.status = 'failed'
            payment.save()
        val /= 0

        return redirect('/maricon/abstract/')
    else:
        return JsonResponse({'status': 'failure'})
