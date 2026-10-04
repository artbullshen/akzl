from django.contrib import admin

# Register your models here.

from .models import Pinlun, Entry, Topic, Enntry

admin.site.register(Pinlun)
admin.site.register(Entry)
admin.site.register(Topic)
admin.site.register(Enntry)
