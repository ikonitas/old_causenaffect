# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OrderLine'
        db.create_table('orders_orderline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Order'])),
            ('songs_pk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Music'])),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('line_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('discounted_line_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
        ))
        db.send_create_signal('orders', ['OrderLine'])

        # Removing M2M table for field songs on 'Order'
        db.delete_table('orders_order_songs')


    def backwards(self, orm):
        
        # Deleting model 'OrderLine'
        db.delete_table('orders_orderline')

        # Adding M2M table for field songs on 'Order'
        db.create_table('orders_order_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['orders.order'], null=False)),
            ('music', models.ForeignKey(orm['music.music'], null=False))
        ))
        db.create_unique('orders_order_songs', ['order_id', 'music_id'])


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
            'tx': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'orders.orderline': {
            'Meta': {'object_name': 'OrderLine'},
            'discounted_line_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Order']"}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'songs_pk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Music']"})
        }
    }

    complete_apps = ['orders']
