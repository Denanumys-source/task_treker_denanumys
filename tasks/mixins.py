from urllib import request
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.messages import success,warning,error

class UserIsOwnerMixin(object):
    owner_field = 'creator'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if getattr(obj,self.owner_field) != request.user:
            redirect('auth_system:login')
            raise PermissionDenied
        
        return super().dispatch(request, *args, **kwargs)
class HiMessageMixin:
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        success(request, f"Привіт, {request.user.username}!")
        return super().dispatch(request,*args,**kwargs)
        