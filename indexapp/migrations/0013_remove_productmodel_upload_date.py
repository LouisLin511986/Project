# Generated by Django 4.0.3 on 2022-05-08 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0012_alter_productmodel_pimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='upload_date',
        ),
    ]