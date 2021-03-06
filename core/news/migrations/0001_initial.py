# Generated by Django 3.2.7 on 2021-09-22 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_type_id', models.CharField(max_length=50)),
                ('dictionary_tokens', models.CharField(max_length=50)),
                ('news_type', models.CharField(max_length=50)),
                ('news_headline', models.TextField(max_length=100)),
                ('news_article', models.TextField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=50)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
