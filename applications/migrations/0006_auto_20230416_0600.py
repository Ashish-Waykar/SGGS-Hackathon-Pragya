# Generated by Django 3.0.6 on 2023-04-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0005_auto_20230416_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='category',
            field=models.CharField(blank=True, choices=[('Request', 'Request'), ('Leave', 'Leave'), ('Other', 'Other'), ('Documents', 'Documents')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(blank=True, choices=[('Accepted Level 1', 'Accepted Level 1'), ('Rejected', 'Rejected'), ('Approoved', 'Approoved'), ('Submited', 'Submited')], max_length=1000, null=True),
        ),
    ]