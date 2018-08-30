# Generated by Django 2.0.3 on 2018-03-21 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20180320_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='stu_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.ClassInfo', verbose_name="Student's Class"),
        ),
    ]
