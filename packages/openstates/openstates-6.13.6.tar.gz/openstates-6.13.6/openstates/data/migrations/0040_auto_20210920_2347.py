# Generated by Django 3.2.2 on 2021-09-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0039_auto_20210920_1934"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventdocumentlink",
            name="document",
        ),
        migrations.RemoveField(
            model_name="eventmedialink",
            name="media",
        ),
        migrations.AddField(
            model_name="eventagendamedia",
            name="links",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="eventdocument",
            name="links",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name="eventmedia",
            name="links",
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.DeleteModel(
            name="EventAgendaMediaLink",
        ),
        migrations.DeleteModel(
            name="EventDocumentLink",
        ),
        migrations.DeleteModel(
            name="EventMediaLink",
        ),
    ]
