# Generated by Django 4.0.7 on 2023-07-26 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_employee'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('first_name', 'last_name')},
        ),
    ]
