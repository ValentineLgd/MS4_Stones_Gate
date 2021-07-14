# Code from Checkout App videos from Boutique Ado lessons #

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ip8wcErc69KbLOdN3dTCepgcdseVY2Kc70gV0zQNBAO0tX4087WG59MUO7fq1wPnyp88ccdr0G3McrRAaQnfCCJ00X5Dir3WP',
        'client_secret': 'test client secret,'
    }

    return render(request, template, context)
