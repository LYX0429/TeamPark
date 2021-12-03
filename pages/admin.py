from django.contrib import admin
import pages
# Register your models here.

admin.site.register(pages.models.Doctor)
admin.site.register(pages.models.Appointment)