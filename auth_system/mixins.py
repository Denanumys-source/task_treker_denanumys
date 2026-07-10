from urllib import request

from django.core.exceptions import PermissionDenied
from django.contrib.messages import success,warning,error


class HiMessageMixin:
    success_message = None
    def dispatch(self, request, *args, **kwargs):
        success(request, self.success_message)
        return super().dispatch(request,*args,**kwargs)