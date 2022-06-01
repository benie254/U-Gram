from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(name,receiver):
    # create message subject & sender
    subject = 'You are subscribed!'
    sender = 'davinci.monalissa3@gmail.com'

    # pass in context variables
    text_content = render_to_string('email/newsemail.txt',{"name":name})
    html_content = render_to_string('email/newsemail.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
