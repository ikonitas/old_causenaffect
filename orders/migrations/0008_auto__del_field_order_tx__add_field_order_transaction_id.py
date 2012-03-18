# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Order.tx'
        db.delete_column('orders_order', 'tx')

        # Adding field 'Order.transaction_id'
        db.add_column('orders_order', 'transaction_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Order.tx'
        db.add_column('orders_order', 'tx', self.gf('django.db.models.fields.CharField')(default=1, max_length=250), keep_default=False)

        # Deleting field 'Order.transaction_id'
        db.delete_column('orders_order', 'transaction_id')


    models = {
        'music.category': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Category'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': "'True'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'music.music': {
            'Meta': {'ordering': "('songs_order',)", 'object_name': 'Music'},
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Cause N Affect'", 'max_length': '50'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Category']", 'null': 'True', 'blank': 'True'}),
            'full_track': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'songs_order': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'track_sample': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'orders.order': {
            'Meta': {'object_name': 'Order'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payer_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'payer_full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'purchased_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '2'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'orders.orderline': {
            'Meta': {'object_name': 'OrderLine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'songs_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'songs_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Music']"})
        }
    }

    complete_apps = ['orders']
