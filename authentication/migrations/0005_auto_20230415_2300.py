# Generated by Django 3.0.6 on 2023-04-15 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20230415_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='department_HOD',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='department',
        ),
        migrations.RemoveField(
            model_name='hod',
            name='user',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='department',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='published_by_director',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='published_by_hod',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.DeleteModel(
            name='application',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='faculty',
        ),
        migrations.DeleteModel(
            name='hod',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]