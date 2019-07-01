from django.contrib import admin
import env_page
# Register your models here.

admin.site.register(env_page.models.Project)
admin.site.register(env_page.models.Product)
admin.site.register(env_page.models.Network)
admin.site.register(env_page.models.UserInfo)
admin.site.register(env_page.models.Server)