# Generated by Django 4.0.2 on 2022-03-31 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0021_employee_employees_e_minoas__771d29_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(db_column='IS_ACTIVE', db_index=True, default=True),
        ),
    ]
