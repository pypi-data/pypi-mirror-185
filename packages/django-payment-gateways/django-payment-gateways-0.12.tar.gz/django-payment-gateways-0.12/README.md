Iraninan Gateways Implemention for Django
=====

## Curently Supports:
1. Parsian Bank
2. Zarinpal

Usage
-----

```python
# Config
PAYMENT_SETTINGS = {
    'drivers': {
        'default': 'parsian',
        'zarinpal': {
            # sandbox
            'sandboxApiPurchaseUrl': 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl',
            'sandboxApiPaymentUrl': 'https://sandbox.zarinpal.com/pg/StartPay/',
            'sandboxApiVerificationUrl': 'https://sandbox.zarinpal.com/pg/services/WebGate/wsdl',

            # normal
            'apiPurchaseUrl': 'https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json',
            'apiPaymentUrl': 'https://www.zarinpal.com/pg/StartPay/',
            'apiVerificationUrl': 'https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json',

            'merchantId': 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX',
            'callbackUrl': 'xxxxxxxxxxxx',
            'description': 'payment in zarinpal',
            'mode': 'sandbox',
        },
        'parsian': {
            # sandbox
            'sandboxApiPurchaseUrl': 'http://banktest.ir/gateway/parsian-sale/ws?wsdl',
            'sandboxApiPaymentUrl': 'http://banktest.ir/gateway/parsian/gate/',
            'sandboxApiVerificationUrl': 'http://banktest.ir/gateway/parsian-confirm/ws?wsdl',

            # normal
            'apiPurchaseUrl': 'https://pec.shaparak.ir/NewIPGServices/Sale/SaleService.asmx?wsdl',
            'apiPaymentUrl': 'https://pec.shaparak.ir/NewIPG/',
            'apiVerificationUrl': 'https://pec.shaparak.ir/NewIPGServices/Confirm/ConfirmService.asmx?wsdl',

            'merchantId': 'xxxxxxx',
            'callbackUrl': 'xxxxxxxxxxxx',
            'description': 'payment in parsian',
            'mode': 'normal',
        },
    },
    'map': {
        'zarinpal': 'payment.modules.drivers.zarinpal:Zarinpal',
        'parsian': 'payment.modules.drivers.parsian:Parsian'
    }
}

# request payment
from django_payment_gateways import PaymentWorker
from django_payment_gateways import Invoice

invoice = Invoice()
invoice.set_amount(order.amount)
invoice.set_details('description', 'پرداخت سفارش')

# generate a unique number
number = generate_unique_digits()

invoice.create_uuid(number)

payment = PaymentWorker()
driver_instance, transaction_id = payment.purchase(invoice)
# save payment data in database
```

# Verify

```python
def post(self, request, *args, **kwargs):
    """
    callback for bank return in payment
    """
    if request.POST.get('status'):
        try:
            payment_obj = Payment.objects.get(reservation=request.POST.get('Token'), paid=False)
        except:
            raise APIException(detail='not found')

        try:
            with transaction.atomic():
                payment_worker = PaymentWorker()
                invoice = Invoice()
                invoice.set_amount(payment_obj.amount)
                invoice.set_transaction_id(payment_obj.reservation)
                payment_worker.set_invoice(invoice)
                receipt, driver_instance = payment_worker.verify(request)

                # payment is successful, Do whatever you want

                return redirect("success url")
        except Exception:
            return redirect('failed url')
    return redirect('failed url')
```