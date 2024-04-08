# Generated by Django 4.2.11 on 2024-04-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0002_dairyfeeds'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dairyfeeds',
            options={'verbose_name': 'Dairy Feed', 'verbose_name_plural': 'Dairy Feeds'},
        ),
        migrations.AlterField(
            model_name='dairyfeeds',
            name='feed_type',
            field=models.CharField(choices=[('hay', 'Hay'), ('silage', 'Silage'), ('dairymeal', 'Dairy Meal'), ('other', 'Other')], max_length=20, verbose_name='Feed Type'),
        ),
        migrations.AlterField(
            model_name='dairyfeeds',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Quantity (kg)'),
        ),
    ]
