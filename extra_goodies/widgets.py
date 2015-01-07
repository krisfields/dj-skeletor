from django import forms
from django.utils.safestring import mark_safe


class ImagePreviewWidget(forms.FileInput):
    """
    A ImageField Widget that shows a thumbnail.
    """

    def __init__(self, height=None, attrs={}):
        if not height:
            height = 100
        self.height = height
        super(ImagePreviewWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            multiplier = float(value.height)/self.height
            width = float(value.width)/multiplier
            output.append(('<a rel="facebox" target="_blank" href="%s">'
                           '<img class="photo" src="%s"'
                           'style="height: %spx; width: %spx" /></a> <br/>'
                           % (value.url, value.url, self.height, width)))
        output.append(super(ImagePreviewWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
