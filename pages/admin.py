from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        exclude = []
        widgets = {
            'content': TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
