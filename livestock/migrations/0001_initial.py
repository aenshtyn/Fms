# Generated by Django 4.2.11 on 2024-04-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='cow', max_length=100)),
                ('last_name', models.CharField(default='cow', max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=80)),
                ('species', models.CharField(choices=[('cattle', 'Cattle'), ('sheep', 'Sheep'), ('goat', 'Goat'), ('poultry', 'Poultry'), ('others', 'Others')], default='cattle', max_length=80)),
                ('breed', models.CharField(default='', max_length=80)),
                ('date_of_birth', models.DateField()),
                ('date_acquired', models.DateField(blank=True, null=True)),
                ('acquisition_source', models.CharField(blank=True, max_length=100)),
                ('acquisition_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_sold', models.DateField(blank=True, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('health_status', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
