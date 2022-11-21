# Generated by Django 4.1 on 2022-11-19 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0003_alter_tariff_unique_together_tariff_flag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tariffs', to='tariffs.distributor'),
        ),
    ]