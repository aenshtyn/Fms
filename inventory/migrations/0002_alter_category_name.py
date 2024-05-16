# Generated by Django 4.2.11 on 2024-05-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('CROP_HC', 'Crops (Human Consumption)'), ('CROP_LF', 'Crops (Livestock Feed)'), ('ANIMAL_PROD', 'Animal Products'), ('FARM_MACH', 'Farm Machinery'), ('TOOLS', 'Tools'), ('FERTILIZERS', 'Fertilizers'), ('PEST_HERB', 'Pesticides and Herbicides'), ('SEEDS', 'Seeds and Planting Materials'), ('ANIMAL_FEED', 'Animal Feed'), ('VET_SUPPLIES', 'Veterinary Supplies'), ('FARM_OPS', 'Farm Operations Supplies'), ('PACKAGING', 'Packaging Materials'), ('CONSTRUCTION', 'Construction Materials'), ('PROTECTIVE', 'Protective Gear')], max_length=50, unique=True),
        ),
    ]
