# Generated by Django 2.0.4 on 2019-07-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_workorderstate_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, '已终止'), (1, '申请中'), (2, '已同意'), (3, '已完成'), (4, '已驳回')], default=1, verbose_name='工单状态'),
        ),
    ]
