from django.contrib import admin
from .models import NewsletterUser
from django.utils.safestring import mark_safe
import threading

class NewsletterAdmin(admin.ModelAdmin):
    list_display=('email', 'date_added')
admin.site.register(NewsletterUser,NewsletterAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display=('email', 'date_added')
# admin.site.register(User,UserAdmin)
