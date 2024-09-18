# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import TestQuestion, UserTestResponse

# Optionally, you can unregister default models if you have custom ones
# admin.site.unregister(Group)

# Register your custom user model or extend the default User model
# Example for extending the default User model:
# admin.site.register(User, BaseUserAdmin)
