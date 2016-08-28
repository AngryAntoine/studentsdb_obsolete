from django.contrib import admin

from .models import Student


class AdminStudent(admin.ModelAdmin):
    pass
    # search_fields = [
    #     'first_name',
    #     'last_name',
    # ]
    # list_display = [
    #     'first_name',
    #     'last_name',
    # ]
    # list_display_links = [
    #     'first_name',
    #     'last_name',
    # ]

admin.site.register(Student)
