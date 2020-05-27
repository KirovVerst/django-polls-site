# Generated by Django 3.0.6 on 2020-05-27 19:59
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("polls", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="choice", name="votes"),
        migrations.CreateModel(
            name="UserChoice",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("choice", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="polls.Choice")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
