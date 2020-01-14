from django.contrib import admin

from .models import GuideTour


class GuideTourAdmin(admin.ModelAdmin):
    pass


admin.site.register(GuideTour, GuideTourAdmin)
