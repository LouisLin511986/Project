# Generated by Django 4.0.5 on 2022-07-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0027_alter_productmodel_pimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='pimages',
            field=models.ImageField(blank=True, default=0, upload_to='image/'),
        ),
    ]