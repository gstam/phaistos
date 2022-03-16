# Generated by Django 3.1.5 on 2021-10-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_auto_20211014_0701'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='employee',
            name='employees_e_EMPLOYE_83fce3_idx',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='type',
            new_name='employee_type',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='maritalType',
            new_name='marital_status',
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['employee_type'], name='employees_e_EMPLOYE_83fce3_idx'),
        ),
    ]