# coding=utf-8
from django.template.loader import render_to_string
from django.core.mail import send_mail


def email_sender(user, course):
    subject = '抢课神器通知'
    to = [user.email]
    from_email = 'psuclass-notice@psuclass.com'

    ctx = {
        'user': user.username,
        'course': course,
        'remaining': user.courses_used - user.courses_caught
    }

    message = render_to_string('email_templates/alert.html', ctx)
    send_mail(subject, '', from_email, to, fail_silently=False, html_message=message)


def email_sender_fail(user):
    subject = '抢课神器通知'
    to = [user.email]
    from_email = 'psuclass-notice@psuclass.com'

    ctx = {
        'user': user.username,
    }

    message = render_to_string('email_templates/fail.html', ctx)
    send_mail(subject, '', from_email, to, fail_silently=False, html_message=message)
