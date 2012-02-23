# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.pub_date'
        db.delete_column('events_event', 'pub_date')

        # Adding field 'Event.event_date'
        db.add_column('events_event', 'event_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 1, 17, 18, 46, 2, 156701)), keep_default=False)

        # Changing field 'Event.time'
        db.alter_column('events_event', 'time', self.gf('django.db.models.fields.TimeField')())


    def backwards(self, orm):
        
        # Adding field 'Event.pub_date'
        db.add_column('events_event', 'pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 1, 17, 18, 37, 40, 901594)), keep_default=False)

        # Deleting field 'Event.event_date'
        db.delete_column('events_event', 'event_date')

        # Changing field 'Event.time'
        db.alter_column('events_event', 'time', self.gf('django.db.models.fields.TimeField')(auto_now=True))


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'event_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 1, 17, 18, 46, 2, 156701)'}),
            'flayer': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flayer_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['events']
