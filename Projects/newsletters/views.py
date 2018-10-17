from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm

# Create a Newsletter
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
                send_mail(subject=subject, from_email=from_email, recipient_list=[newsletteruser.email], message=body, fail_silently=True)
            messages.success(request, 'The newsletter has been created', 'alert alert-success alert-dismissable')
            return redirect('control_newsletter_detail', pk=newsletter.pk)

    context = {
        "form": form,
    }

    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

# Edit a Newsletter
def control_newsletter_edit(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == "POST":
        form = NewsletterCreationForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save()
            if newsletter.status == 'Published':
                subject = newsletter.subject
                body = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for newsletteruser in newsletter.email.all():
                    send_mail(subject=subject, from_email=from_email, recipient_list=[newsletteruser.email], message=body, fail_silently=True)
                messages.success(request, 'The newsletter has been updated', 'alert alert-success alert-dismissable')
            return redirect('control_newsletter_detail', pk=newsletter.pk)
    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {
        "form": form,
    }

    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

# def control_newsletter_edit(request, pk):
#     newsletter = get_object_or_404(Newsletter, pk=pk)
#
#     if request.method == "POST":
#         form = NewsletterCreationForm(request.POST, instance=newsletter)
#         if form.is_valid():
#             newsletter = form.save()
#             if newsletter.status == 'Published':
#                 subject = newsletter.subject
#                 body = newsletter.body
#                 from_email = settings.EMAIL_HOST_USER
#                 for newsletteruser in newsletter.email.all():
#                     send_mail(subject=subject, from_email=from_email, recipient_list=[newsletteruser.email], message=body, fail_silently=True)
#                 messages.success(request, 'The newsletter has been updated', 'alert alert-success alert-dismissable')
#             return redirect('control_newsletter_detail', pk=newsletter.pk)
#     else:
#         form = NewsletterCreationForm(instance=newsletter)
#
#     context = {
#         "form": form,
#     }
#
#     template = 'control_panel/control_newsletter.html'
#     return render(request, template, context)

# Newsletter Sign Up
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
            message = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to_email)
            html_template = get_template("newsletters/signup_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        's_form': s_form,
    }
    template = 'newsletters/signup.html'
    return render(request, template, context)

# Newsletter Unsubscribe
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
            # with open(settings.BASE_DIR + "/newsletters/templates/newsletters/unsubscribe_email.txt") as f:
            #     signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, from_email=from_email, to=to_email)
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

# Display ALL Newsletters
def control_newsletter_list(request):
    newsletters = Newsletter.objects.all()
    paginator = Paginator(newsletters, 5)
    page = (request.GET.get('page'))

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= max_index -5 else 0
    end_index = index + 5 if index <= max_index -5 else max_index
    page_range = paginator.page_range[start_index:end_index]


    context = {
        "items": items,
        "page_range": page_range
    }
    template = "control_panel/control_newsletter_list.html"
    return render(request,template, context)

# Single Newsletter Detail
def control_newsletter_detail(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    context = {
    "newsletter": newsletter,
    }
    template = "control_panel/control_newsletter_detail.html"
    return render(request, template, context)

# Delete a Newsletter
def control_newsletter_delete(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if request.method == "POST":
        form = NewsletterCreationForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter.delete()
            return redirect('control_newsletter_list')

    else:
        form = NewsletterCreationForm(instance=newsletter)

    context = {
        "form": form,
    }
    template = 'control_panel/control_newsletter_delete.html'
    return render(request, template, context)
