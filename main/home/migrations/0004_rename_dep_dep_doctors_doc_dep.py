# Generated by Django 4.2.7 on 2023-11-14 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_dep_name_doctors_dep_dep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='dep_dep',
            new_name='doc_dep',
        ),
    ]