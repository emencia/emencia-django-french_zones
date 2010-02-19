"""Admin for emencia.django.french_zones"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.french_zones.models import Region
from emencia.django.french_zones.models import Department

class DepartmentInline(admin.StackedInline):
    model = Department

class RegionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'departments')
    fields = ('code', 'name',)
    inlines = [DepartmentInline]
    actions_on_top = False
    actions_on_bottom = True

    def departments(self, region):
        return ', '.join([d.name for d in region.department_set.all()])

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'code', 'region')
    fields = ('region', 'code', 'name')
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Region, RegionAdmin)
admin.site.register(Department, DepartmentAdmin)

