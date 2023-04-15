# Generated by Django 3.0.6 on 2023-04-15 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1st Year', '1st Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('2nd Year', '2nd Year')], max_length=300)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hod.department')),
                ('user', models.ForeignKey(limit_choices_to={'is_student': True}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
