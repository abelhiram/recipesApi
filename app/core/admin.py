"""django admin ustomization"""

from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """define the admin pages for users"""
    order = ['id']
    list_display = ['email','name']

