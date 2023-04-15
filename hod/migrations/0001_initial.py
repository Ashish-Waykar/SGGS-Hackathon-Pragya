# Generated by Django 3.0.6 on 2023-04-15 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('Civil', 'Civil'), ('Electronics', 'Electronics'), ('Chemical', 'Chemical'), ('Textile', 'Textile'), ('Production', 'Production'), ('Mechanical', 'Mechanical'), ('Information Technology', 'Information Technology'), ('Computer Science', 'Computer Science')], max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('department_HOD', models.ForeignKey(blank=True, limit_choices_to={'is_faculty': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hod.department')),
                ('user', models.ForeignKey(limit_choices_to={'is_hod': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]