# Generated by Django 3.1.4 on 2021-01-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventMan', '0005_auto_20210110_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='deadline',
            field=models.CharField(max_length=122),
        ),
    ]
