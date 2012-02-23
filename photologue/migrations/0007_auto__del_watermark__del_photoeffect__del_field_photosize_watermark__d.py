# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Watermark'
        db.delete_table('photologue_watermark')

        # Deleting model 'PhotoEffect'
        db.delete_table('photologue_photoeffect')

        # Deleting field 'PhotoSize.watermark'
        db.delete_column('photologue_photosize', 'watermark_id')

        # Deleting field 'PhotoSize.effect'
        db.delete_column('photologue_photosize', 'effect_id')

        # Deleting field 'Photo.effect'
        db.delete_column('photologue_photo', 'effect_id')


    def backwards(self, orm):
        
        # Adding model 'Watermark'
        db.create_table('photologue_watermark', (
            ('opacity', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('style', self.gf('django.db.models.fields.CharField')(default='scale', max_length=5)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
        ))
        db.send_create_signal('photologue', ['Watermark'])

        # Adding model 'PhotoEffect'
        db.create_table('photologue_photoeffect', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reflection_strength', self.gf('django.db.models.fields.FloatField')(default=0.6)),
            ('color', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('sharpness', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('filters', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(default='#FFFFFF', max_length=7)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('brightness', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('reflection_size', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('transpose_method', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('contrast', self.gf('django.db.models.fields.FloatField')(default=1.0)),
        ))
        db.send_create_signal('photologue', ['PhotoEffect'])

        # Adding field 'PhotoSize.watermark'
        db.add_column('photologue_photosize', 'watermark', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_sizes', null=True, to=orm['photologue.Watermark'], blank=True), keep_default=False)

        # Adding field 'PhotoSize.effect'
        db.add_column('photologue_photosize', 'effect', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_sizes', null=True, to=orm['photologue.PhotoEffect'], blank=True), keep_default=False)

        # Adding field 'Photo.effect'
        db.add_column('photologue_photo', 'effect', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photo_related', null=True, to=orm['photologue.PhotoEffect'], blank=True), keep_default=False)


    models = {
        'photologue.gallery': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Gallery'},
            'album_cover': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'cover'", 'unique': 'True', 'null': 'True', 'to': "orm['photologue.Photo']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photologue.Photo']"}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'photologue.galleryupload': {
            'Meta': {'object_name': 'GalleryUpload'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'photologue.photosize': {
            'Meta': {'ordering': "['width', 'height']", 'object_name': 'PhotoSize'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment_count': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'pre_cache': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quality': ('django.db.models.fields.PositiveIntegerField', [], {'default': '70'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['photologue']
