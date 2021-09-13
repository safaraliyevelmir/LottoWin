from .models import Contact, ContactInformation, ContactTitle
from django.contrib import admin





class ContactAdmin(admin.ModelAdmin):

    list_display = ['name','email','date']
    list_filter = ['date']
    search_fields = ['name']


admin.site.register(Contact,ContactAdmin)
admin.site.register(ContactInformation)
admin.site.register(ContactTitle)