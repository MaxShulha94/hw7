# Generated by Django 4.2.5 on 2023-10-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school_info", "0004_alter_student_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
