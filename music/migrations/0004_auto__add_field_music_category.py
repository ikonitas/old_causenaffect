# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Music.category'
        db.add_column('music_music', 'category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Categories'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Music.category'
        db.delete_column('music_music', 'category_id')


    models = {
        'music.categories': {
            'Meta': {'object_name': 'Categories'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': "'True'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'music.music': {
            'Meta': {'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Categories']", 'null': 'True', 'blank': 'True'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['music']
