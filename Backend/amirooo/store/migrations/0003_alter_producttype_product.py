# Generated by Django 4.2.4 on 2024-01-30 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_producttype_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_types', to='store.product'),
        ),
    ]
