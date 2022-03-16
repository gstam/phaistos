# Generated by Django 3.1.5 on 2021-10-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='big_family',
            field=models.BooleanField(db_column='BIG_FAMILY', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='comment',
            field=models.CharField(db_column='COMMENT', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(db_column='EMAIL', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_man',
            field=models.BooleanField(db_column='MAN', null=True),
        ),
    ]