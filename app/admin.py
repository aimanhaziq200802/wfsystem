from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.site_url = "/home"
admin.site.register(Quotation)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Entity)