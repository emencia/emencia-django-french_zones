"""Unit tests for emencia.django.french_zones"""
from django.test import TestCase

from emencia.django.french_zones.models import Region, Region2016
from emencia.django.french_zones.models import Department
from emencia.django.french_zones.utils import get_region_from_postal_code
from emencia.django.french_zones.utils import get_region_2016_from_postal_code
from emencia.django.french_zones.utils import get_department_from_postal_code

class UtilsTestCase(TestCase):

    def test_get_department_from_postal_code(self):
        self.assertRaises(ValueError, get_department_from_postal_code, '')
        self.assertRaises(ValueError, get_department_from_postal_code, '1234')

        pas_de_calais = Department.objects.get(pk='62')
        paris = Department.objects.get(pk='75')
        corse_du_sud = Department.objects.get(pk='2A')
        reunion = Department.objects.get(pk='974')

        self.assertEquals(get_department_from_postal_code('62138'), pas_de_calais)
        self.assertEquals(get_department_from_postal_code('75012'), paris)
        self.assertEquals(get_department_from_postal_code('20600'), corse_du_sud)
        self.assertEquals(get_department_from_postal_code('97412'), reunion)

    def test_get_region_from_postal_code(self):
        self.assertRaises(ValueError, get_region_from_postal_code, '')
        self.assertRaises(ValueError, get_region_from_postal_code, '1234')

        nord_pas_de_calais = Region.objects.get(pk='31')
        ile_de_france = Region.objects.get(pk='11')
        corse = Region.objects.get(pk='94')
        guadeloupe = Region.objects.get(pk='01')

        self.assertEquals(get_region_from_postal_code('62138'), nord_pas_de_calais)
        self.assertEquals(get_region_from_postal_code('75012'), ile_de_france)
        self.assertEquals(get_region_from_postal_code('20600'), corse)
        self.assertEquals(get_region_from_postal_code('97105'), guadeloupe)

    def test_get_region2016_from_postal_code(self):
        self.assertRaises(ValueError, get_region_2016_from_postal_code, '')
        self.assertRaises(ValueError, get_region_2016_from_postal_code, '1234')

        nord_pas_de_calais_picardie = Region2016.objects.get(pk='32')
        ile_de_france = Region2016.objects.get(pk='11')
        corse = Region2016.objects.get(pk='94')
        guadeloupe = Region2016.objects.get(pk='01')
        aquitaine_limousin_poitou_charentes = Region2016.objects.get(pk='75')

        self.assertEquals(get_region_2016_from_postal_code('62138'),
                          nord_pas_de_calais_picardie)
        self.assertEquals(get_region_2016_from_postal_code('75012'),
                          ile_de_france)
        self.assertEquals(get_region_2016_from_postal_code('20600'), corse)
        self.assertEquals(get_region_2016_from_postal_code('97105'),
                          guadeloupe)
        self.assertEquals(get_region_2016_from_postal_code('23001'),
                          aquitaine_limousin_poitou_charentes)
