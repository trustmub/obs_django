# Generated by Django 2.0.6 on 2018-07-14 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['customer_id'], 'verbose_name_plural': 'accounts'},
        ),
    ]