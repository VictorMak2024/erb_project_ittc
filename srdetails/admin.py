from django.contrib import admin

from .models import Srdetail

class SrdetailAdmin(admin.ModelAdmin):
    list_display = ('id','items_no','itemsname',)
    list_display_links = 'items_no',
    list_editable = 'itemsname',
    search_fields = 'itemsname',
    list_per_page = 25

admin.site.register(Srdetail, SrdetailAdmin)