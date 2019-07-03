from django.contrib import admin
from .models import information

admin.site.register(information)

admin.site.site_header = "IT CRATS -> ADMIN-PANEL"
admin.site.index_title = "APPLICANTS INFORMATION"
