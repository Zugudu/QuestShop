from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('In-game info'), {'fields': ('money',)}),
		)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(_('In-game info'), {'fields': ('money',)}),
		)



admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.Artifact)