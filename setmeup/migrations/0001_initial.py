# Generated by Django 4.1.5 on 2023-01-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("duedate", models.DateTimeField(null=True)),
                ("noidung", models.TextField(null=True)),
                (
                    "kind",
                    models.SmallIntegerField(
                        choices=[(1, "Khẩn"), (2, "Đột xuất"), (3, "Định kỳ")]
                    ),
                ),
                (
                    "dinhky",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Tháng"),
                            (2, "Quý"),
                            (3, "Năm"),
                            (4, "6 tháng"),
                            (5, "9 tháng"),
                        ],
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-pk"],
            },
        ),
        migrations.CreateModel(
            name="NoiNhan",
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
        migrations.CreateModel(
            name="PhongBan",
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
                ("name", models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name="Title",
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
