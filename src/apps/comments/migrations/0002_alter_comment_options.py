# Generated by Django 4.2.9 on 2024-02-04 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]
