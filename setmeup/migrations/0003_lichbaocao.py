# Generated by Django 4.1.5 on 2023-01-13 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("setmeup", "0002_noinhan"),
    ]

    operations = [
        migrations.CreateModel(
            name="LichBaoCao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
