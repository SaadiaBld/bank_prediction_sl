from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ModelApi

admin.site.register(User, UserAdmin)
#admin.site.register(ModelApi)
