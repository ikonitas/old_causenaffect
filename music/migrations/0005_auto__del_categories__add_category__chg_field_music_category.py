# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Categories'
        db.delete_table('music_categories')

        # Adding model 'Category'
        db.create_table('music_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add='True', blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=20, db_index=True)),
        ))
        db.send_create_signal('music', ['Category'])

        # Changing field 'Music.category'
        db.alter_column('music_music', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Category'], null=True))


    def backwards(self, orm):
        
        # Adding model 'Categories'
        db.create_table('music_categories', (
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add='True', blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=20, db_index=True)),
        ))
        db.send_create_signal('music', ['Categories'])

        # Deleting model 'Category'
        db.delete_table('music_category')

        # Changing field 'Music.category'
        db.alter_column('music_music', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Categories'], null=True))


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['music']
