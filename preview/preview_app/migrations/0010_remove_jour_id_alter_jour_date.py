# Generated by Django 4.1.7 on 2023-04-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preview_app', '0009_jour_id_alter_jour_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jour',
            name='id',
        ),
        migrations.AlterField(
            model_name='jour',
            name='date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]
