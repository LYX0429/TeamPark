from django.contrib import admin
import pages
# Register your models here.

admin.site.register(pages.models.Project)
admin.site.register(pages.models.Product)
admin.site.register(pages.models.Network)
admin.site.register(pages.models.UserInfo)
admin.site.register(pages.models.Server)