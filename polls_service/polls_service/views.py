from .utils import ErrorList


class BaseView:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["error_class"] = ErrorList
        return kwargs
