# Generated by Django 3.0 on 2019-12-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191206_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='OtherInfo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]