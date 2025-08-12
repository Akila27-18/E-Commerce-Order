from django.shortcuts import render, redirect
from .forms import OrderForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
import random

def index(request):
    order_form = OrderForm()
    contact_form = ContactForm()
    order_success = contact_success = None

    if request.method == 'POST':
        if 'order_submit' in request.POST:
            order_form = OrderForm(request.POST)
            if order_form.is_valid():
                name = order_form.cleaned_data['name']
                email = order_form.cleaned_data['email']
                total_amount = order_form.cleaned_data['total_amount']
                order_id = random.randint(100000, 999999)

                # Send order confirmation email
                subject = f"Order Confirmation #{order_id}"
                message = f"Hi {name},\n\nThank you for your order.\nOrder ID: {order_id}\nTotal Amount: ${total_amount}\n\nWe will process your order soon.\n\nBest regards,\nE-Commerce Team"
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

                order_success = f"Order placed successfully! A confirmation email has been sent to {email}."
                order_form = OrderForm()  # reset form

        elif 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                message_text = contact_form.cleaned_data['message']

                # Send contact email to admin
                subject = f"Customer Query from {name}"
                message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])

                contact_success = "Your message has been sent to admin. We'll get back to you shortly."
                contact_form = ContactForm()  # reset form

    context = {
        'order_form': order_form,
        'contact_form': contact_form,
        'order_success': order_success,
        'contact_success': contact_success,
    }
    return render(request, 'orders/index.html', context)
