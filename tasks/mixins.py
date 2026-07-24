from urllib import request
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.messages import success,warning,error

class UserIsOwnerMixin(object):
    owner_field = 'creator'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if getattr(obj,self.owner_field) != request.user:
            raise PermissionDenied
            
        
        return super().dispatch(request, *args, **kwargs)
class HiMessageMixin:
    text_mixin = None
    def dispatch(self, request, *args, **kwargs):
        text = self.text_mixin
        success(request,text)
        return super().dispatch(request,*args,**kwargs)
    def handle_no_premision(self):
        messages.error(self.request, self.text_mixin)
        return super().handle_no_permission()
        