# Generated by Django 4.1.1 on 2022-10-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_quote_options_remove_quote_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={},
        ),
        migrations.RemoveField(
            model_name='quote',
            name='created_at',
        ),
    ]
