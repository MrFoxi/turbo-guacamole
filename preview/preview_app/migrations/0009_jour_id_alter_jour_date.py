# Generated by Django 4.1.7 on 2023-04-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preview_app', '0008_remove_session_date_session_duree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jour',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jour',
            name='date',
            field=models.DateField(),
        ),
    ]