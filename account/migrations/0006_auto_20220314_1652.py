# Generated by Django 3.0 on 2022-03-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200501_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee')], max_length=10),
        ),
    ]
