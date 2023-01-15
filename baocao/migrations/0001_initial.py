# Generated by Django 4.1.5 on 2023-01-14 14:56

import baocao.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaoCao",
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
                ("noidung", models.TextField()),
                ("nguoi_duyet", models.CharField(max_length=255)),
                ("nguoi_ky", models.CharField(max_length=255)),
                ("thoigian", models.DateTimeField()),
                ("note", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MediaFile",
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
                (
                    "media",
                    models.FileField(upload_to=baocao.models.media_directory_path),
                ),
                (
                    "baocao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="baocao.baocao"
                    ),
                ),
            ],
        ),
    ]
