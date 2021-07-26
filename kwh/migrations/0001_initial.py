# Generated by Django 3.2.5 on 2021-07-26 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FemsTrans',
            fields=[
                ('site_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('dev_id', models.CharField(max_length=128)),
                ('transaction_id', models.CharField(max_length=20)),
                ('dev_time', models.CharField(max_length=128)),
                ('eng_type', models.IntegerField()),
                ('version', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'fems_trans',
            },
        ),
        migrations.CreateModel(
            name='FemsPayload',
            fields=[
                ('payload_id', models.AutoField(primary_key=True, serialize=False)),
                ('dev_id', models.CharField(max_length=128)),
                ('dev_time', models.CharField(max_length=128)),
                ('payload_data', models.TextField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='siteid', to='kwh.femstrans')),
            ],
            options={
                'db_table': 'fems_payload',
            },
        ),
    ]
