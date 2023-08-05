# Generated by Django 3.0.5 on 2020-10-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0027_auto_20200923_1329"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="email",
            field=models.CharField(
                blank=True,
                default="",
                help_text="The official email address of the Person.",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="personcontactdetail",
            name="value",
            field=models.CharField(
                help_text="The content of the Contact information like a phone number or address.",
                max_length=300,
            ),
        ),
    ]
