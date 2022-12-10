# Generated by Django 4.1.2 on 2022-12-08 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Group ID ')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Group Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Room ID')),
                ('room_name', models.CharField(max_length=250, verbose_name='Room Name')),
                ('password', models.CharField(blank=True, max_length=250, verbose_name='Password')),
                ('is_research', models.BooleanField(default=True, verbose_name='Research')),
                ('players', models.TextField(blank=True, verbose_name='players')),
                ('host', models.TextField(blank=True, verbose_name='host')),
                ('done_host_list', models.TextField(blank=True, verbose_name='Done Hosting')),
                ('online', models.TextField(blank=True, verbose_name='Online')),
                ('arithmetic', models.TextField(blank=True, verbose_name='Arithmetic')),
                ('difficulty', models.TextField(blank=True, verbose_name='difficulty')),
                ('speed', models.TextField(blank=True, verbose_name='Speed')),
                ('lvl', models.TextField(blank=True, verbose_name='lvl')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='revise_multiplayer.group', verbose_name='Group Name')),
            ],
        ),
    ]
