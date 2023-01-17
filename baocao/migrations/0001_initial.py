# Generated by Django 4.1.5 on 2023-01-17 01:31

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
                ("note", models.TextField()),
                ("thoigian", models.DateTimeField()),
            ],
            options={
                "ordering": ["-pk"],
            },
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
                ("filename", models.CharField(max_length=255, null=True)),
                ("filetype", models.CharField(max_length=255, null=True)),
                (
                    "baocao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="baocao.baocao"
                    ),
                ),
            ],
        ),
    ]
