from django.contrib import admin
from .models import NewsletterUser, Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_Added')

admin.site.register(NewsletterUser, NewsletterAdmin)
admin.site.register(Newsletter)
