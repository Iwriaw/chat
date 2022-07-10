from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
ADDITIONAL_FIELDS = ((None, {'fields': ('nick_name', 'register_time')}),)


class NewUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS
    add_fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS


admin.site.register(User, NewUserAdmin)
