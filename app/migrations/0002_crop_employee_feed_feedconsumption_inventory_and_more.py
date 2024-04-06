# Generated by Django 4.2.11 on 2024-04-06 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('variety', models.CharField(blank=True, max_length=100, null=True)),
                ('planting_date', models.DateField()),
                ('harvest_date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=50)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True)),
                ('feeds_livestock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='cow', max_length=100)),
                ('last_name', models.CharField(default='cow', max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=80)),
                ('department', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('feed_type', models.CharField(choices=[('hay', 'Hay'), ('silage', 'Silage'), ('dairymeal', 'Dairy Meal'), ('other', 'Other')], default='other', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=20)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('purchase_date', models.DateField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_consumed', models.DateField(default=django.utils.timezone.now)),
                ('quantity_consumed', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(max_length=20)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('minimum_stock_level', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
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
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
        migrations.AddField(
            model_name='feedconsumption',
            name='feed_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.inventory'),
        ),
        migrations.AddField(
            model_name='feedconsumption',
            name='livestock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livestock'),
        ),
    ]
