# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.utils.text import slugify

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        for reg in orm.Region.objects.all():
            reg.slug = slugify(reg.name)
            reg.save()
        for dep in orm.Department.objects.all():
            dep.slug = slugify(dep.name)
            dep.save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
