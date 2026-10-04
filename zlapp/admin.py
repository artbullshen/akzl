from django.contrib import admin

# Register your models here.

from .models import News, Topic, Entry

admin.site.register(News)
admin.site.register(Topic)
admin.site.register(Entry)




