# Generated by Django 2.2.12 on 2021-02-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='jumlah',
            field=models.IntegerField(null=True),
        ),
    ]
