from django.contrib import admin

from zip.models import ZipCode


@admin.register(ZipCode)
class ZipCodeAdmin(admin.ModelAdmin):
    list_display = ["code", "country", "city"]
    search_fields = ["code", "country", "city"]
