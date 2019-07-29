# Generated by Django 2.0.4 on 2019-07-24 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_auto_20190723_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.UUID('2964aea9-1c7a-4e5a-ab16-3bd31a1a12bd'), verbose_name='用户jwt加密秘钥'),
        ),
    ]
