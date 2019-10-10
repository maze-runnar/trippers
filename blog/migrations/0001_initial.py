# Generated by Django 2.2 on 2019-07-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
