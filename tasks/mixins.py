from urllib import request

from django.core.exceptions import PermissionDenied
from django.contrib.messages import success,warning,error

class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.creator != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class HiMessageMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        success(request, f"Привіт, {request.user.username}!")
        return super().dispatch(request,*args,**kwargs)
        