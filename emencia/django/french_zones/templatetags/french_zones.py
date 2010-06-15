"""Templatetags for emencia.django.french_zones"""
from django.template import Node
from django.template import Library
from django.template import Variable
from django.template import VariableDoesNotExist

from emencia.django.french_zones.utils import get_region_from_postal_code
from emencia.django.french_zones.utils import get_department_from_postal_code

register = Library()

class PostalCodeSetterNode(Node):
    """Node for settings something in the context
    based on a postal code variable"""
    def __init__(self, postal_code, varname):
        self.postal_code, self.varname = Variable(postal_code), varname
        
    def render(self, context):
        try:
            context[self.varname] = self.process(self.postal_code.resolve(context))
        except VariableDoesNotExist, ValueError:
            pass
        return ''

class DepartmentSetterNode(PostalCodeSetterNode):
    """Return department model instance in the context
    based on postal code"""

    def process(self, postal_code):
        return get_department_from_postal_code(postal_code)

class RegionSetterNode(PostalCodeSetterNode):
    """Return region model instance in the context
    based on postal code"""

    def process(self, postal_code):
        return get_region_from_postal_code(postal_code)


@register.tag
def get_department(parser, token):
    """{% get_department_from_postal_code postal_code as var %}"""
    bits = token.split_contents()
    
    if len(bits) != 4:
        raise TemplateSyntaxError, "get_department_from_postal_code tag takes exactly three arguments"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "second argument to get_department_from_postal_code tag must be 'as'"
    return DepartmentSetterNode(bits[1], bits[3])

        
@register.tag
def get_region(parser, token):
    """{% get_region_from_postal_code postal_code as var %}"""
    bits = token.split_contents()
    
    if len(bits) != 4:
        raise TemplateSyntaxError, "get_region_from_postal_code tag takes exactly three arguments"
    if bits[2] != 'as':
        raise TemplateSyntaxError, "second argument to get_region_from_postal_code tag must be 'as'"
    return RegionSetterNode(bits[1], bits[3])









                                                                        
