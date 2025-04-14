from django.contrib import admin
from .models import Applicant
from django.utils.html import format_html

#Register your models here

class ApplicantAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email', 'phone', 'apply_date', 'title', 'company', 'job_id', 'cv_file_link'
    def cv_file_link(self, obj):
        if obj.cv_file:
            return format_html('<a href="{}" target="_blank">Download CV</a>', obj.cv_file.url)
        return "No file uploaded"
    cv_file_link.short_description = "CV File"
    list_display_links = 'id', 'name'
    readonly_fields = 'user_id', 'job_id'
    search_fields = 'name', 'email', 'title', 'company'
    list_per_page = 25

admin.site.register(Applicant, ApplicantAdmin)