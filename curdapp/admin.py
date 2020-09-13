from django.contrib import admin
from curdapp.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display=['no','name','salary','address']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
