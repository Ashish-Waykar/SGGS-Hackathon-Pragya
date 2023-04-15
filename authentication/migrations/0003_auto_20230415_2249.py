# Generated by Django 3.0.6 on 2023-04-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230415_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='publisher',
            new_name='publisher_user',
        ),
        migrations.AlterField(
            model_name='application',
            name='category',
            field=models.CharField(blank=True, choices=[('Submited', 'Submited'), ('Approoved', 'Approoved'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='content',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('Submited', 'Submited'), ('Approoved', 'Approoved'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(choices=[('Chemical', 'Chemical'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'), ('Information Technology', 'Information Technology'), ('Computer Science', 'Computer Science'), ('Electronics', 'Electronics')], max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('3rd Year', '3rd Year'), ('2nd Year', '2nd Year'), ('4th Year', '4th Year')], max_length=300),
        ),
    ]