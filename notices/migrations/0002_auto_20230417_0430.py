# Generated by Django 3.0.6 on 2023-04-16 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='published_by_director',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='published_by_hod',
        ),
        migrations.AddField(
            model_name='notice',
            name='content',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='for_director_to',
            field=models.CharField(blank=True, choices=[('For Faculty(Director)', 'For Faculty(Director)'), ('For Department HOD (Director)', 'For Department HOD (Director)'), ('Whole College(Director)', 'Whole College(Director)'), ('For Year(Director)', 'For Year(Director)')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='from_head_user_by',
            field=models.CharField(blank=True, choices=[('HOD', 'HOD'), ('Director', 'Director')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='from_hod_to',
            field=models.CharField(blank=True, choices=[('For Student(HOD)', 'For Student(HOD)'), ('For Department(HOD)', 'For Department(HOD)'), ('For Faculty(HOD)', 'For Faculty(HOD)')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='notice_image',
            field=models.ImageField(blank=True, null=True, upload_to='notice_images/'),
        ),
        migrations.AddField(
            model_name='notice',
            name='publish_to_yr',
            field=models.CharField(blank=True, choices=[('4th Year', '4th Year'), ('3rd Year', '3rd Year'), ('2nd Year', '2nd Year'), ('1st Year', '1st Year')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='published_to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
