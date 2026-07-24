from urllib import request

from django.core.exceptions import PermissionDenied
from django.contrib.messages import success,warning,error

from tasks.mixins import HiMessageMixin