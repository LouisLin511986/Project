# Generated by Django 4.1.1 on 2022-12-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0069_remove_authorized_checkbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorized',
            name='File',
            field=models.FileField(blank=True, default=0, null=True, upload_to='file', verbose_name='檔案'),
        ),
        migrations.AddField(
            model_name='authorized',
            name='username',
            field=models.CharField(blank=True, max_length=20, verbose_name='購物者'),
        ),
    ]
