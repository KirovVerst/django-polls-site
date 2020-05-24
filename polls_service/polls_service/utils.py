from django.forms import utils
from django.utils.html import format_html_join


class ErrorList(utils.ErrorList):
    def __init__(self, *args, **kwargs):
        kwargs["error_class"] = "alert alert-danger"
        super(ErrorList, self).__init__(*args, **kwargs)

    def as_ul(self):
        if not self.data:
            return ""

        return format_html_join("", '<p class="{}">{}</p>', ((self.error_class, e) for e in self))
