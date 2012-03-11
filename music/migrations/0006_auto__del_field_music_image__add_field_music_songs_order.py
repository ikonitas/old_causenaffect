# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Music.image'
        db.delete_column('music_music', 'image')

        # Adding field 'Music.songs_order'
        db.add_column('music_music', 'songs_order', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Music.image'
        db.add_column('music_music', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'Music.songs_order'
        db.delete_column('music_music', 'songs_order')


    models = {
        'music.category': {
            'Meta': {'object_name': 'Category'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': "'True'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'music.music': {
            'Meta': {'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Category']", 'null': 'True', 'blank': 'True'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'songs_order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['music']
