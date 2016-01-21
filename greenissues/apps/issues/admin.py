from django.contrib import admin
from apps.issues import models
# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_header = "MBSSE TAE  Green Issues"

admin_site = MyAdminSite(name='myadmin')
admin_site.register(models.Issues)
admin_site.register(models.Solutions)


# admin.site.register(models.Issues)
# admin.site.register(models.Solutions)
