# Generated by Django 4.2.6 on 2023-11-16 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_booking_doc_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_email', models.EmailField(max_length=254)),
                ('c_description', models.TextField()),
            ],
        ),
    ]