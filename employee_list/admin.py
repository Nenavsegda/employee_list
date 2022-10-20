from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from employee_list.models import Department, Employee


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Employee)
admin.site.register(Department, DjangoMpttAdmin)
