# Generated by Django 4.2.11 on 2024-04-12 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0006_remove_breeding_expected_due_date'),
        ('dairy', '0005_rename_dairyfeeds_feeds_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='production',
            unique_together={('cow', 'milking_date')},
        ),
    ]
