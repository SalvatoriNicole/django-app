# Generated by Django 4.1 on 2023-07-12 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blackrot", "0003_remove_state_ons_t0_state_ons_clus_t0_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="state",
            name="DD_10_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="state",
            name="DD_6_24_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="state",
            name="DD_9_25_t0",
            field=models.FloatField(default=0),
        ),
    ]
