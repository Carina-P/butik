from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IX166JKlvgFF1ppZywzGgXRLOalVYSY6XpGTCwLoQx1BJK36QkRFZPzzceMo7noBEjnva5vEQCnz2fP1lCfmulp00Ieu64lFN',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
