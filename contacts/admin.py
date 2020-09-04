from django.contrib import admin

from .models import *

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class CompanyContactAdmin(admin.ModelAdmin):
  list_display = ('company_email', 'company_phone', 'company_location')
  list_display_links = ('company_email', 'company_phone')
  search_fields = ('company_email', 'company_phone')

admin.site.register(CompanyContact, CompanyContactAdmin)
