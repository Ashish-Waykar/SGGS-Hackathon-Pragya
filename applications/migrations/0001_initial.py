# Generated by Django 3.0.6 on 2023-04-15 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hod', '0003_auto_20230415_2315'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Rejected', 'Rejected'), ('Approoved', 'Approoved'), ('Accepted Level 1', 'Accepted Level 1'), ('Submited', 'Submited')], max_length=1000, null=True)),
                ('category', models.CharField(blank=True, choices=[('Rejected', 'Rejected'), ('Approoved', 'Approoved'), ('Accepted Level 1', 'Accepted Level 1'), ('Submited', 'Submited')], max_length=1000, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
                ('reject_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_by_faculty', models.BooleanField(default=False)),
                ('is_by_student', models.BooleanField(default=False)),
                ('is_rejected_by_director', models.BooleanField(default=False)),
                ('is_rejected_by_hod', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hod.department')),
                ('publisher_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]