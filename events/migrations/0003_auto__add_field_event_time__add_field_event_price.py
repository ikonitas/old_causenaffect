# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Event.time'
        db.add_column('events_event', 'time', self.gf('django.db.models.fields.TimeField')(auto_now=True, default=datetime.datetime(2012, 1, 17, 18, 43, 0, 616879)), keep_default=False)

        # Adding field 'Event.price'
        db.add_column('events_event', 'price', self.gf('django.db.models.fields.CharField')(default=0, max_length=10), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Event.time'
        db.delete_column('events_event', 'time')

        # Deleting field 'Event.price'
        db.delete_column('events_event', 'price')


    models = {
        'events.event': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Event'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'flayer': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flayer_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 1, 17, 18, 37, 40, 901594)'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'time': ('django.db.models.fields.TimeField', [], {'auto_now': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['events']
