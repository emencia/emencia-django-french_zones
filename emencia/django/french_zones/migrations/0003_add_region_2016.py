# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.utils.text import slugify

from emencia.django.french_zones.models import Region, Department


class Migration(DataMigration):

    def forwards(self, orm):
        # Create region2016 model
        # Add region2016 data
        db.create_table(u'french_zones_region_2016', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=12, blank=True)),
        ))
        db.send_create_signal(u'french_zones', ['Region2016'])

        # Add region2016 field to regions
        db.add_column(
            u'french_zones_region', 'region_2016',
            self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['french_zones.Region2016'], null=True
            ),
            keep_default=False
        )

        # Add region2016 field to departments
        db.add_column(
            u'french_zones_department', 'region_2016',
            self.gf('django.db.models.fields.related.ForeignKey')(
                to=orm['french_zones.Region2016'], null=True
            ),
            keep_default=False
        )

    def backwards(self, orm):
        db.delete_table(u'french_zones_region_2016')
        db.delete_column(u'french_zones_region', 'region2016_id')
        db.delete_column(u'french_zones_department', 'region2016_id')

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
