# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Event.pub_date'
        db.add_column('events_event', 'pub_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 1, 18, 20, 48, 10, 389192), auto_now=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Event.pub_date'
        db.delete_column('events_event', 'pub_date')


    models = {
        'events.event': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Event'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'event_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 1, 18, 20, 48, 10, 389217)'}),
            'flayer': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flayer_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 1, 18, 20, 48, 10, 389192)', 'auto_now': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'time': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['events']
