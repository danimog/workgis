# Generated by Django 2.2.3 on 2019-08-02 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcoapp', '0007_auto_20190802_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dettaglio',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parcoapp.Entry'),
        ),
    ]
