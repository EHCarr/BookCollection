# Generated by Django 4.1.1 on 2022-10-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_quote_options_remove_quote_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]