# Generated by Django 3.1.5 on 2021-01-21 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('description', models.CharField(db_column='DESCRIPTION', max_length=255, null=True)),
                ('legacy_code', models.CharField(db_column='LEGACY_CODE', max_length=32)),
                ('suitable_for_employee_type', models.CharField(choices=[('DEPUTY', 'Αναπληρωτής'), ('REGULAR', 'Μόνιμος'), ('HOURLYPAID', 'Ωρομίσθιος'), ('ADMINISTRATIVE', 'Διοικητικός')], db_column='EMPLOYEE_TYPE', default='REGULAR', max_length=32)),
                ('basic_type', models.CharField(choices=[('UNPAID_LEAVE', 'Άνευ Αποδοχών'), ('REGULAR_LEAVE', 'Κανονική Άδεια'), ('HOURLYPAID', 'Γενική Άδεια')], db_column='BASIC_TYPE', default='REGULAR_LEAVE', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_column='IS_ACTIVE', default=True)),
                ('comment', models.TextField(db_column='COMMENT', null=True)),
                ('date_from', models.DateField(db_column='DATE_FROM')),
                ('date_until', models.DateField(db_column='DATE_UNTIL')),
                ('effective_number_of_days', models.IntegerField(db_column='EFFECTIVE_DAYS_COUNT', null=True)),
                ('number_of_days', models.IntegerField(db_column='DAYS_COUNT', null=True)),
                ('employee', models.ForeignKey(db_column='EMPLOYEE_ID', on_delete=django.db.models.deletion.PROTECT, to='employees.employee')),
                ('leave_type', models.ForeignKey(db_column='EMPLOYEE_LEAVE_TYPE_ID', on_delete=django.db.models.deletion.PROTECT, to='leaves.leavetype')),
            ],
        ),
    ]
