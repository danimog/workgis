# Generated by Django 2.2.3 on 2019-08-02 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parcoapp', '0005_entry_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='dettaglio',
            name='point',
            field=models.ForeignKey(default='5t', on_delete=django.db.models.deletion.CASCADE, to='parcoapp.Entry'),
        ),
    ]
