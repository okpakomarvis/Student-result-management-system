# Generated by Django 4.1.1 on 2022-09-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20220919_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_roll',
            new_name='student_matric_no',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_date_of_birth',
            field=models.DateField(),
        ),
    ]
