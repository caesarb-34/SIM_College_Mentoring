from django.contrib import admin

from .models import Mentor

class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'start_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Mentor, MentorAdmin)