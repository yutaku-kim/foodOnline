# Generated by Django 3.2.5 on 2024-01-23 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_openinghour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghour',
            options={'ordering': ('day', '-from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='openinghour',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]
