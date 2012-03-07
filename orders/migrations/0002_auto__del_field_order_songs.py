# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Order.songs'
        db.delete_column('orders_order', 'songs_id')

        # Adding M2M table for field songs on 'Order'
        db.create_table('orders_order_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm['orders.order'], null=False)),
            ('music', models.ForeignKey(orm['music.music'], null=False))
        ))
        db.create_unique('orders_order_songs', ['order_id', 'music_id'])


    def backwards(self, orm):
        
        # Adding field 'Order.songs'
        db.add_column('orders_order', 'songs', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['music.Music']), keep_default=False)

        # Removing M2M table for field songs on 'Order'
        db.delete_table('orders_order_songs')


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
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Music']", 'symmetrical': 'False'}),
            'tx': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['orders']
