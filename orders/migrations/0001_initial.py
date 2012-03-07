# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Order'
        db.create_table('orders_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('songs', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Music'])),
            ('purchased_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('tx', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('orders', ['Order'])


    def backwards(self, orm):
        
        # Deleting model 'Order'
        db.delete_table('orders_order')


    models = {
        'music.music': {
            'Meta': {'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchased_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'songs': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Music']"}),
            'tx': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['orders']
