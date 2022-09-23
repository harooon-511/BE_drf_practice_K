from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("nickname","username", "password",)}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("nickname","username", "password1", "password2",),
            },
        ),
    )
    list_display = ("id","username", "nickname", "is_staff","is_active",)
    list_filter = ("is_staff", "is_superuser","groups",)
    search_fields = ("username","email",)
    ordering = ("username",)

CustomUser = get_user_model()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
admin.site.register(NotificationModel)
admin.site.register(Friendlist)

# Register your models here.
