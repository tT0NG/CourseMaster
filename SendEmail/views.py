from django.template.loader import render_to_string
from django.core.mail import send_mail

def email_sender_view(request):
    subject = 'test'
    to = ['steveleelx@gmail.com']
    from_email = 'psuclass-notice@psuclass.com'

    ctx = {
        'user': 'steve',
    }

    message = render_to_string('email_templates/alert.html', ctx)
    print 'before send'
    send_mail(subject, '', from_email, to, fail_silently=False, html_message=message)
    return

def email_sender(request, user, course):
    subject = 'test'
    to = [user.email]
    from_email = 'psuclass-notice@psuclass.com'

    ctx = {
        'user': user.username,
        'course': course,
        'remaining': user.courses_used - user.courses_caught
    }

    message = render_to_string('email_templates/alert.html', ctx)
    print 'before send'
    send_mail(subject, '', from_email, to, fail_silently=False, html_message=message)
    return
