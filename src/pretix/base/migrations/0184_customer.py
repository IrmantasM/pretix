# Generated by Django 3.0.13 on 2021-04-06 07:25

import django.db.models.deletion
from django.db import migrations, models

import pretix.base.models.base


def set_can_manage_customers(apps, schema_editor):
    Team = apps.get_model('pretixbase', 'Team')
    Team.objects.filter(can_change_organizer_settings=True).update(can_manage_customers=True)
    Team.objects.filter(can_change_orders=True, all_events=True).update(can_manage_customers=True)


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0183_auto_20210423_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('identifier', models.CharField(db_index=True, max_length=190, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=190, null=True)),
                ('password', models.CharField(max_length=128)),
                ('name_cached', models.CharField(max_length=255)),
                ('name_parts', models.JSONField(default=dict)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('locale', models.CharField(default='en', max_length=50)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='pretixbase.Organizer')),
            ],
            options={
                'unique_together': {('organizer', 'email')},
            },
            bases=(models.Model, pretix.base.models.base.LoggingMixin),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='pretixbase.Customer'),
        ),
        migrations.AddField(
            model_name='team',
            name='can_manage_customers',
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(
            set_can_manage_customers,
            migrations.RunPython.noop,
        ),
    ]
