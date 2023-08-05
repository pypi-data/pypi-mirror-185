# Generated by Django 3.0.5 on 2020-09-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0017_remove_person_summary"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bill",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="event",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="jurisdiction",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="membership",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="person",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="post",
            name="locked_fields",
        ),
        migrations.RemoveField(
            model_name="voteevent",
            name="locked_fields",
        ),
    ]
