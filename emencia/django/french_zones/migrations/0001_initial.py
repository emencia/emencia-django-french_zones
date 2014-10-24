# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'french_zones_region', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=2, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128, blank=True)),
        ))
        db.send_create_signal(u'french_zones', ['Region'])

        # Adding model 'Department'
        db.create_table(u'french_zones_department', (
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['french_zones.Region'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128, blank=True)),
        ))
        db.send_create_signal(u'french_zones', ['Department'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'french_zones_region')

        # Deleting model 'Department'
        db.delete_table(u'french_zones_department')


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