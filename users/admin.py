from django.contrib import admin
from .models import User
from custom_user.admin import EmailUserAdmin
from django.db import models
from extra_goodies.widgets import ImagePreviewWidget
import reversion


class UserAdmin(EmailUserAdmin, reversion.VersionAdmin):
    list_display = ['email_image', 'first_name', 'last_name', 'date_joined']
    fieldsets = EmailUserAdmin.fieldsets
    fieldsets = list(fieldsets)
    personal_information = ("Personal info", {
                            'fields': ('first_name', 'last_name', 'image', 'about')
                            })
    fieldsets.insert(1, personal_information)
    fieldsets = tuple(fieldsets)
    ordering = ('-date_joined',)
    search_fields = ('first_name', 'last_name', 'email')
    formfield_overrides = {models.ImageField: {'widget': ImagePreviewWidget}, }

    def email_image(self, obj):
        if obj.image:
            return u'<img width="100px" src="%s"><br />%s' % (obj.image.url, obj.email)
        return obj.email
    email_image.allow_tags = True
    email_image.short_description = "Email"
    email_image.admin_order_field = "email"

admin.site.register(User, UserAdmin)
