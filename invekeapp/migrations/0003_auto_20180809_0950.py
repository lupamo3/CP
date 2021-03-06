# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-09 06:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invekeapp', '0002_faq_opportunity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, max_length=4000, null=True)),
                ('summary', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('H', 'Hidden'), ('P', 'Published')], max_length=10)),
                ('start_publication', models.DateTimeField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('edited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('pubdat', models.DateField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['singlea']},
        ),
        migrations.AddField(
            model_name='faq',
            name='image',
            field=models.ImageField(default=1234, upload_to='img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='singlea',
            field=tinymce.models.HTMLField(default=1234),
            preserve_default=False,
        ),
    ]
