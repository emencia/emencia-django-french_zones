# -*- coding: utf-8 -*-
from south.v2 import SchemaMigration
from django.core.management import call_command
from django.utils._os import upath

from os.path import join, dirname

from emencia.django.french_zones.models import Region, Department, Region2016
from emencia.django import french_zones


REGION_TRANSLATION_DICT = {
    u'01': u'01',
    u'02': u'02',
    u'03': u'03',
    u'04': u'04',
    u'06': u'06',
    u'11': u'11',
    u'21': u'44',
    u'22': u'32',
    u'23': u'28',
    u'24': u'24',
    u'25': u'28',
    u'26': u'27',
    u'31': u'32',
    u'41': u'44',
    u'42': u'44',
    u'43': u'27',
    u'52': u'52',
    u'53': u'53',
    u'54': u'75',
    u'72': u'75',
    u'73': u'76',
    u'74': u'75',
    u'82': u'84',
    u'83': u'84',
    u'91': u'76',
    u'93': u'93',
    u'94': u'94',
}


def region_2016_from_region_2015(region_2015):
    try:
        code_2016 = REGION_TRANSLATION_DICT[region_2015.code]
        region_2016 = Region2016.objects.get(code=code_2016)
        return region_2016
    except KeyError:
        region_2016 = Region2016(code=region_2015.code, name=region_2015.name,
                                 slug=region_2015.slug)
        region_2016.save()
        return region_2016


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Add Region2016 data
        fixture_file = upath(
            join(dirname(french_zones.__file__),
                 "fixtures/2016_evolution_data.xml")
        )
        call_command("loaddata", fixture_file)

        # Set region_2016 fields to regions
        for region in Region.objects.all():
            region.region_2016 = region_2016_from_region_2015(region)
            region.save()

        # Set region_2016 fields to departments
        for department in Department.objects.all():
            region = department.region
            department.region_2016 = region.region_2016
            department.save()

    def backwards(self, orm):
        pass


    models = {
        u'french_zones.department': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Department'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['french_zones.Region']"}),
            'region_2016': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['french_zones.Region2016']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'french_zones.region': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region_2016': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['french_zones.Region2016']", 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'french_zones.region2016': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Region2016'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['french_zones']
