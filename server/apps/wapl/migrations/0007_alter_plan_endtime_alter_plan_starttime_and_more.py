# Generated by Django 4.1.5 on 2023-02-01 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapl', '0006_remove_user_image_alter_plan_endtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='endTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='startTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='title',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(0, '제목은 반드시 입력해야 합니다.')]),
        ),
    ]
