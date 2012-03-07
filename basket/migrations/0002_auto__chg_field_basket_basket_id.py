# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Basket.basket_id'
        db.alter_column('basket_basket', 'basket_id', self.gf('django.db.models.fields.CharField')(max_length=500))


    def backwards(self, orm):
        
        # Changing field 'Basket.basket_id'
        db.alter_column('basket_basket', 'basket_id', self.gf('django.db.models.fields.CharField')(max_length=50))


    models = {
        'basket.basket': {
            'Meta': {'ordering': "['date_added']", 'object_name': 'Basket'},
            'basket_id': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'song'", 'unique': 'True', 'to': "orm['music.Music']"})
        },
        'music.music': {
            'Meta': {'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['basket']
