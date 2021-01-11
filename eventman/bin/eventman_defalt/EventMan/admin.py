from django.contrib import admin
from EventMan.models import register,partregister,hosts

# Register your models here.
admin.site.register(register)
admin.site.register(partregister)
admin.site.register(hosts)