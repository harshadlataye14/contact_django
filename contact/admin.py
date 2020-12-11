from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','Name','gender','email','info','phone')
    list_editable = ('info',)
    search_field = ('Name','gender','email','info','phone')
    list_filter = ('gender','date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)

