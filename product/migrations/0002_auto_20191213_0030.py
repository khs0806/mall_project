# Generated by Django 3.0 on 2019-12-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stuck',
            new_name='stock',
        ),
    ]