# Generated by Django 3.1.6 on 2021-02-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelion', '0002_auto_20210128_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_pass',
            field=models.IntegerField(default=2),
        ),
    ]
