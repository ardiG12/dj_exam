from django.contrib import admin
from project.models import CustomUser, Profile

from django.contrib.auth.admin import UserAdmin

admin.site.register([Profile])

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name' ,'email', 'is_staff', 'is_superuser')

    add_fieldsets = (
        ('CreateUser', {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )