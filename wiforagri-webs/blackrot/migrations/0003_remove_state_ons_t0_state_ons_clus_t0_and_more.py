# Generated by Django 4.1 on 2023-07-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blackrot", "0002_rename_h_post_t0_state_h_postr_t0"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="state",
            name="ONS_t0",
        ),
        migrations.AddField(
            model_name="state",
            name="ONS_clus_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="state",
            name="ONS_leaf_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="daily",
            name="GS",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="daily",
            name="hod",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="daily",
            name="humidity",
            field=models.FloatField(default=10),
        ),
        migrations.AlterField(
            model_name="daily",
            name="leafwetness",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="daily",
            name="rain",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="daily",
            name="temperature",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="daily",
            name="treatment",
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name="data",
            name="doy",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="data",
            name="year",
            field=models.FloatField(default=2000),
        ),
        migrations.AlterField(
            model_name="state",
            name="ASCmat_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="COMmat_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="H_postr_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="H_rain_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="Hdry_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="RH_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="SEV_asco_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="SEV_con_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="WD_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="doy",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="state",
            name="wetness_t0",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="state",
            name="year",
            field=models.FloatField(default=2000),
        ),
    ]
