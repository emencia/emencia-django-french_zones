"""Admin for emencia.django.french_zones"""
from django.contrib import admin
from django.utils.translation import ugettext as _

from emencia.django.french_zones.models import Region
from emencia.django.french_zones.models import Region2016
from emencia.django.french_zones.models import Department

class DepartmentInline(admin.StackedInline):
    model = Department

class Region2016Admin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'code', 'departments')
    fields = ('code', 'name',)
    inlines = [DepartmentInline]
    actions_on_top = False
    actions_on_bottom = True

    def departments(self, region):
        return ', '.join([d.name for d in region.department_set.all()])

class RegionAdmin(Region2016Admin):
    list_display = ('name', 'code', 'region_2016', 'departments')
    fields = ('code', 'name', 'region_2016')

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')
    list_display = ('name', 'code', 'region')
    fields = ('region', 'code', 'name')
    actions_on_top = False
    actions_on_bottom = True

admin.site.register(Region2016, Region2016Admin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Department, DepartmentAdmin)

