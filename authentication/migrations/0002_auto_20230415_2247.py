# Generated by Django 3.0.6 on 2023-04-15 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='category',
            field=models.CharField(blank=True, choices=[('Approoved', 'Approoved'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Submited', 'Submited')], max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('Approoved', 'Approoved'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Submited', 'Submited')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Mechanical', 'Mechanical'), ('Computer Science', 'Computer Science'), ('Information Technology', 'Information Technology'), ('Civil', 'Civil'), ('Chemical', 'Chemical')], max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], max_length=300),
        ),
    ]
