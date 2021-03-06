# Generated by Django 2.1.1 on 2018-11-14 15:26

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


def change_refunded_to_canceled(apps, schema_editor):
    Order = apps.get_model('pretixbase', 'Order')
    Order.objects.filter(status='r').update(status='c')


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0103_auto_20181121_1224'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='orderposition',
            managers=[
                ('all', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='orderposition',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderfee',
            name='fee_type',
            field=models.CharField(choices=[('payment', 'Payment fee'), ('shipping', 'Shipping fee'), ('service', 'Service fee'), ('cancellation', 'Cancellation fee'), ('other', 'Other fees'), ('giftcard', 'Gift card')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderposition',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='all_positions',
                                    to='pretixbase.Order', verbose_name='Order'),
        ),
        migrations.AlterModelManagers(
            name='orderfee',
            managers=[
                ('all', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='orderfee',
            name='canceled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderfee',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='all_fees', to='pretixbase.Order', verbose_name='Order'),
        ),
        migrations.RunPython(
            change_refunded_to_canceled, migrations.RunPython.noop
        )
    ]
