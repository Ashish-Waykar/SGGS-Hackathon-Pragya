# Generated by Django 3.0.6 on 2023-04-16 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hod', '0007_auto_20230416_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_HOD',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_hod': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Chemical', 'Chemical'), ('Production', 'Production'), ('Textile', 'Textile'), ('Information Technology', 'Information Technology'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Electronics', 'Electronics'), ('Computer Science', 'Computer Science')], max_length=300),
        ),
    ]
