from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    exclude = ('created', 'updated')
    list_display = ('id', 'name', 'second_name', 'phone', 'email_address', 'created', 'updated')

admin.site.register(Address, AddressAdmin)
