# Generated by Django 3.2.12 on 2022-07-05 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cyprusark', '0015_alter_person_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='media',
        ),
    ]
