# Generated by Django 3.1.4 on 2021-01-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventMan', '0003_partregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=12)),
                ('h_id', models.CharField(default='ho1', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='partregister',
            name='number',
            field=models.CharField(default='1', max_length=122),
        ),
    ]
