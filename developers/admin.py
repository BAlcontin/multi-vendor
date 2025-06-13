from django.contrib import admin
from developers.models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('user', 'developer_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'developer_name')
    list_editable = ('is_approved',)


admin.site.register(Developer, DeveloperAdmin)
