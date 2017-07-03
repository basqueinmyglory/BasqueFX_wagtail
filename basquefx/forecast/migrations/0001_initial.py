# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='forecast',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(verbose_name='Post date')),
                ('strong_cur', models.CharField(choices=[('USD', 'USD'), ('GBP', 'GBP'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('CAD', 'CAD'), ('AUD', 'AUD'), ('NZD', 'NZD'), ('---', '---')], default='USD', max_length=3)),
                ('strong_reason', wagtail.wagtailcore.fields.RichTextField()),
                ('weak_cur', models.CharField(choices=[('USD', 'USD'), ('GBP', 'GBP'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('CAD', 'CAD'), ('AUD', 'AUD'), ('NZD', 'NZD'), ('---', '---')], default='USD', max_length=3)),
                ('weak_reason', wagtail.wagtailcore.fields.RichTextField()),
                ('notes', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
