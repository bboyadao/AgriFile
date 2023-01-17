# Generated by Django 4.1.5 on 2023-01-17 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("setmeup", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="lichbaocao",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="lichbaocao",
            name="phongban",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="setmeup.phongban"
            ),
        ),
    ]
