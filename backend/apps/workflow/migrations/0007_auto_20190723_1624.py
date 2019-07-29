# Generated by Django 2.0.4 on 2019-07-23 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20190723_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_prefix', models.CharField(blank=True, default='OpsOnline', max_length=128, null=True, verbose_name='工单号前缀')),
                ('order_type', models.CharField(blank=True, max_length=128, null=True, verbose_name='工单类型')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='主题')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '已终止'), (1, '申请中'), (2, '已同意'), (3, '已驳回')], default=1, verbose_name='工单状态')),
                ('content', models.TextField(blank=True, verbose_name='工单参数')),
                ('describe', models.TextField(blank=True, verbose_name='描述')),
                ('creator', models.CharField(blank=True, max_length=50, verbose_name='申请人')),
                ('operation_group', models.CharField(blank=True, max_length=50, verbose_name='操作组')),
                ('operator', models.CharField(blank=True, max_length=50, verbose_name='操作人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '工单表',
                'verbose_name_plural': '工单表',
            },
        ),
        migrations.CreateModel(
            name='WorkOrderState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=50, verbose_name='操作动作')),
                ('operator', models.CharField(blank=True, max_length=50, verbose_name='操作人')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('comment', models.CharField(blank=True, max_length=64, null=True, verbose_name='备注')),
                ('wordorder_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='state_gitwordorder_id', to='workflow.WorkOrder', verbose_name='Git工单id')),
            ],
            options={
                'verbose_name': '工单流转表',
                'verbose_name_plural': '工单流转表',
            },
        ),
        migrations.RemoveField(
            model_name='gitworkorderstate',
            name='gitwordorder_id',
        ),
        migrations.DeleteModel(
            name='GitWorkOrder',
        ),
        migrations.DeleteModel(
            name='GitWorkOrderState',
        ),
    ]
