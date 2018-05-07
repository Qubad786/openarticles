from django.contrib import admin

from web.accounts.models import User


class UserAdmin(admin.ModelAdmin):
    """
    Admin for User data model.
    """
    list_display = ('username', 'gender')

    model = User

    verbose_name = 'User'
    verbose_name_plural = 'Users'


admin.site.register(User, UserAdmin)
