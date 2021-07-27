# Code from Checkout App videos from Boutique Ado lessons #

from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
