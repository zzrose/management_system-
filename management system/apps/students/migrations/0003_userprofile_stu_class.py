# Generated by Django 2.0.3 on 2018-03-19 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180316_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='stu_class',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='students.ClassInfo', verbose_name="Student's Class"),
        ),
    ]
