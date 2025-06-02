# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'full_name', 'user_type', 'verified', 'is_staff', 'created_at')
    list_filter = ('user_type', 'verified', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'phone', 'user_type', 'school_id_image', 'profile_photo', 'bio', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'verified', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'user_type', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'full_name')
    ordering = ('-created_at',)

admin.site.register(User, UserAdmin)
