# Generated by Django 3.0.6 on 2023-04-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20230415_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('3rd Year', '3rd Year'), ('2nd Year', '2nd Year'), ('4th Year', '4th Year'), ('1st Year', '1st Year')], max_length=300),
        ),
    ]
