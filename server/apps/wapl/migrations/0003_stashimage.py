# Generated by Django 4.1.6 on 2023-02-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapl', '0002_alter_share_is_share'),
    ]

    operations = [
        migrations.CreateModel(
            name='StashImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='stash')),
            ],
        ),
    ]
