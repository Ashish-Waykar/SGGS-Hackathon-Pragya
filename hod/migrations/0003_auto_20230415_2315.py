# Generated by Django 3.0.6 on 2023-04-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0002_auto_20230415_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Computer Science', 'Computer Science'), ('Information Technology', 'Information Technology'), ('Production', 'Production'), ('Textile', 'Textile'), ('Mechanical', 'Mechanical'), ('Chemical', 'Chemical'), ('Electronics', 'Electronics'), ('Civil', 'Civil')], max_length=300),
        ),
    ]
