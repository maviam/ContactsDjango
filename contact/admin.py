from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','mobile_phone')
    ordering = ('-first_name',)
    list_filter = ('created_date',)
    search_fields = ('first_name','mobile_phone')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ("-id",)