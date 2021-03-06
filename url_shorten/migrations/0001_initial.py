# Generated by Django 3.0.3 on 2020-02-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.URLField(null=True, verbose_name='Short url')),
                ('long_url', models.URLField(null=True, verbose_name='Long url')),
                ('long_url_encoded', models.CharField(max_length=100, null=True, verbose_name='Long url encoded')),
            ],
        ),
    ]
