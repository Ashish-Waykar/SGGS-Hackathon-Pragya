# Generated by Django 3.0.6 on 2023-04-16 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0009_alter_department_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Production', 'Production'), ('Textile', 'Textile'), ('Electronics', 'Electronics'), ('Information Technology', 'Information Technology'), ('Chemical', 'Chemical'), ('Civil', 'Civil'), ('Computer Science', 'Computer Science'), ('Mechanical', 'Mechanical')], max_length=300),
        ),
    ]