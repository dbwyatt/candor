from django import forms
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from datetime import datetime
import helpers
from helpers import login_required
import json
import os
import requests
import homepage.models as hmod
import sell.models as smod
import stripe

templater = get_renderer('sell')


@view_function
# @login_required()
def process_request(request):
    params = {}
    params['environment'] = helpers.get_environment()

    if request.method == 'POST':
        # This is the Stripe test API key. This would need to be replaced with a real key.
        stripe.api_key = "sk_test_IP7fzzONV3UhA6kjowHXI3hJ"

        # checkout.js generates this token and includes it in the POST request.
        # token = request.POST['stripeToken']

        # Creating a Customer.
        # See this documentation: https://stripe.com/docs/tutorials/charges#saving-credit-card-details-for-later
        # customer = stripe.Customer.create(
        #     source=token,
        #     description="Test Customer"
        # )

        # Adding the Customer ID to our database.
        # smod.StripeCustomer.objects.create(
        #     owner=hmod.Users.objects.filter(id=request.session['user']['id']).first(),
        #     customer_id=customer.id
        # )

        # This is an example of charging the customer later.
        stripe.Charge.create(
            amount=2000,  # in cents
            currency="usd",
            source={
                "number": "4242424242424242",
                "exp_month": 12,
                "exp_year": 2017,
                "cvc": '123'
            },
            description="Charge for test@example.com"
            # customer=smod.StripeCustomer.objects.first().customer_id  # Actually find the right user on this line.
        )

    return templater.render_to_response(request, 'stripe.html', params)
