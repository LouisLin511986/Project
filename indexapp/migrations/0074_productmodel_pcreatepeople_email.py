# Generated by Django 4.1.1 on 2022-12-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0073_rename_username_authorized_buyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='pcreatepeople_email',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='新增者郵箱'),
        ),
    ]
