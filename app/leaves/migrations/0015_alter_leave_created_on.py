# Generated by Django 4.0.2 on 2022-03-31 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0014_leave_leaves_leav_minoas__223ffa_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='created_on',
            field=models.DateTimeField(db_column='CREATED_ON', default=django.utils.timezone.now),
        ),
    ]
