# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Music'
        db.create_table('music_music', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_track', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('track_sample', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('artist', self.gf('django.db.models.fields.CharField')(default='Cause N Affect', max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('music', ['Music'])


    def backwards(self, orm):
        
        # Deleting model 'Music'
        db.delete_table('music_music')


    models = {
        'music.music': {
            'Meta': {'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['music']
