# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-18 14:18
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0088_fix_wrong_parameter_in_page_chooser_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField([(b'case_studies', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'case_studies', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('page', wagtail.wagtailcore.blocks.PageChooserBlock('torchbox.WorkPage')), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('descriptive_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])))])), (b'highlights', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'highlights', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.TextBlock()))])), (b'pull_quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.CharBlock(classname='quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock())], template='blocks/pull_quote_block.html')), (b'process', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=False)), (b'steps', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('icon', wagtail.wagtailcore.blocks.CharBlock(help_text='Paste SVG code here', max_length=9000, required=True)), ('description', wagtail.wagtailcore.blocks.TextBlock(required=True))])))])), (b'people', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'intro', wagtail.wagtailcore.blocks.TextBlock(required=True)), (b'people', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock()))])), (b'featured_pages', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock()), (b'pages', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([('page', wagtail.wagtailcore.blocks.PageChooserBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('sub_text', wagtail.wagtailcore.blocks.CharBlock(max_length=100))])))]))]),
        ),
    ]
