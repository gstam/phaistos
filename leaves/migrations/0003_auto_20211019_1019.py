# Generated by Django 3.1.5 on 2021-10-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0002_auto_20211019_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavetype',
            name='description',
            field=models.CharField(db_column='DESCRIPTION', db_index=True, max_length=255, null=True),
        ),
    ]
