from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm

def newsletter_signup(request):
    s_form = NewsletterUserSignUpForm(request.POST or None)
    if s_form.is_valid():
        instance = s_form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your email already exists in our database', 'alert alert-warning alert-dismissable')
        else:
            instance.save()
            messages.success(request, 'You have been subscribed to the newsletter', 'alert alert-success alert-dismissable')
            subject = "Thank you for Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/signup_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/signup_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        's_form': s_form,
    }
    template = 'newsletters/signup.html'
    return render(request, template, context)

def newsletter_unsubscribe(request):
    u_form = NewsletterUserSignUpForm(request.POST or None)
    if u_form.is_valid():
        instance = u_form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'You have successfully unsubscribed', 'alert alert-success alert-dismissable')
            subject = "You have been successfully unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletters/templates/newsletters/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:
            messages.warning(request, 'Your email is not in our database', 'alert alert-warning alert-dismissable')
    context = {
        'u_form': u_form,
    }
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)

def control_newsletter(request):
    form = NewsletterCreationForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == "Published":
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for newsletteruser in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[newsletteruser.email], message=body)

    context = {
        "form": form,
    }
    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)
