# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Department.slug'
        db.add_column(u'french_zones_department', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Region.slug'
        db.add_column(u'french_zones_region', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=128, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Department.slug'
        db.delete_column(u'french_zones_department', 'slug')

        # Deleting field 'Region.slug'
        db.delete_column(u'french_zones_region', 'slug')


    models = {
        u'french_zones.department': {
            'Meta': {'ordering': "('code',)", 'object_name': 'Department'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['french_zones.Region']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'french_zones.region': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Region'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['french_zones']
