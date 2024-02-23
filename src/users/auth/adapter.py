from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import generate_otp
from django.http import HttpResponseRedirect


class CustomAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        # Generate OTP for the user
        email = emailconfirmation.email_address
        otp = generate_otp(email,6) 

        current_site = get_current_site(request)
        ctx = {
            "user": emailconfirmation.email_address.user,
            "otp": otp,  # Include OTP in the context
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        subject = render_to_string('email/email_confirmation_otp_subject.txt').strip()
        message_plain = render_to_string('email/email_confirmation_otp.txt', ctx)
        message_html = render_to_string('email/email_confirmation_otp.html', ctx)
        send_mail(subject, message_plain, None, [emailconfirmation.email_address.email], html_message=message_html)
        
    def respond_email_verification_sent(self, request, user):
        # Don't redirect user to the email verification sent page and redirect ot otp checkpage
        return HttpResponseRedirect(reverse("account_otp_verification_sent"))
