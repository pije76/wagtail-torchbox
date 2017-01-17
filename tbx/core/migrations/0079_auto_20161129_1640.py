# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-29 16:40
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0078_auto_20161129_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField([(b'case_studies', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'case_studies', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('page', wagtail.wagtailcore.blocks.PageChooserBlock(['torchbox.WorkPage'])), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('descriptive_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])))])), (b'highlights', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'highlights', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.TextBlock()))])), (b'pull_quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock())], template='blocks/pull_quote_block.html')), (b'process', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'steps', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Paste SVG code here', max_length=9000, required=True)), ('description', wagtail.wagtailcore.blocks.TextBlock(required=True))])))])), (b'people', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock()))]))]),
        ),
    ]