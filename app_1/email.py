from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name, email, review):

    context = {
        'name': name,
        'email': email,
        'review': review
    }

    subject = 'Thank you for your review'
    body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )

    return email.send(fail_silently=False)
