# Generated by Django 3.0.1 on 2020-01-01 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concierge', '0005_auto_20200101_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='concierge.Person'),
        ),
    ]
