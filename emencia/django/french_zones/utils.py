"""Utils for emencia.django.french_zones"""
from django.utils.translation import ugettext as _

from emencia.django.french_zones.models import Region
from emencia.django.french_zones.models import Department

def get_department_from_postal_code(postal_code):
    """Return the Region model associated to a postal code"""
    if len(postal_code) != 5:
        raise ValueError, _('Invalid postal code')

    code = postal_code[:2]
    if code == '20':
        code =  '2A'
    if code == '97':
        code = postal_code[:3]
    
    return Department.objects.get(code=code)

def get_region_from_postal_code(postal_code):
    """Return the Department model associated to a postal code"""
    return get_region_from_postal_code(postal_code).region



        
