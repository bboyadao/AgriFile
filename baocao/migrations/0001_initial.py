# Generated by Django 4.1.5 on 2023-01-31 08:32

import baocao.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


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
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-pk"],
            },
            managers=[
                ("thongke", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="ThongKe",
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
                ("created_at", models.DateTimeField(auto_created=True, null=True)),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "kind",
                    models.SmallIntegerField(
                        choices=[(1, "Tháng"), (2, "Quý"), (3, "Năm")]
                    ),
                ),
                ("val", models.SmallIntegerField()),
                ("nam", models.SmallIntegerField(null=True)),
                ("count", models.IntegerField(default=0)),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                ("baocao", models.ManyToManyField(to="baocao.baocao")),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="baocao.thongke",
                    ),
                ),
            ],
            options={
                "abstract": False,
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
