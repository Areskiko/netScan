# Generated by Django 3.0.8 on 2020-07-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arko', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='ip',
        ),
        migrations.AlterField(
            model_name='device',
            name='lastSeen',
            field=models.DateTimeField(auto_now=True),
        ),
    ]