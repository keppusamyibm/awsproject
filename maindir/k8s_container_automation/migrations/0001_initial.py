# Generated by Django 2.1 on 2019-03-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster_runner',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['user_name'],
            },
        ),
    ]
