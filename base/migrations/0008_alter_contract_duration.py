# Generated by Django 4.0.3 on 2022-04-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_merge_20220410_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]