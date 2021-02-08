from django.contrib import admin
from .models import Profile


class ProfileRedactor(admin.ModelAdmin):
    list_display = ('pk', 'user', 'bio')


admin.site.register(Profile, ProfileRedactor)
