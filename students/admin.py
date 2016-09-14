# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Student, Group


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


class AdminGroup(admin.ModelAdmin):
    pass

admin.site.register(Group)
