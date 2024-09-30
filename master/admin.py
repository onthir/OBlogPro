from django.contrib import admin

from .models import *


admin.site.register(Category)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', )
    list_filter = ('category', 'date')
    search_fields = ['title', 'date', 'category']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Notification)
admin.site.register(MailingList)