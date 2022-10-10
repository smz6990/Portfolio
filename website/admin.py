from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    fields = ["name", "email", "subject", "message"]
    list_display = ["name", "email", "subject"]
    list_filter = ["email", "subject"]
    search_fields = ["name", "email", "subject", "message"]
