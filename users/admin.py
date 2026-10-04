"""
这是以前的程序，这样的结果是管理程序中密码显现为明文，
并且增加的新用户（明文密码），也无法登录。
from django.contrib import admin

# Register your models here.

from .models import User
admin.site.register(User)

"""
# 下面是修改后的程序，能够密码（哈希算法）加密。
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin #这是关键
from django.utils.translation import gettext_lazy
from .models import User

# Register your models here.

class UserpAdmin(UserAdmin):
    list_display = ('username','last_login','is_superuser','is_staff','is_active','date_joined')
    fieldsets = (
        (None,{'fields':('username','password','first_name','last_name','email')}),
        (gettext_lazy('User Information'),{'fields':('nickname','wechat')}),
        (gettext_lazy('Permissions'),{'fields':('is_superuser','is_staff','is_active',
                             'groups','user_permissions')}),
        (gettext_lazy('Important dates'),{'fields':('last_login','date_joined')}),
        )


admin.site.register(User,UserpAdmin)
