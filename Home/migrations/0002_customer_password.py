# Generated by Django 4.2 on 2023-04-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="password",
            field=models.CharField(max_length=50, null=True),
        ),
    ]