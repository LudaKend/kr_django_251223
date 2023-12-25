# Generated by Django 5.0 on 2023-12-25 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spammer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spammer_name', models.CharField(max_length=100, verbose_name='ФИО менеджера')),
                ('company', models.TextField(blank=True, null=True, verbose_name='Компания')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email менеджера')),
                ('is_active', models.BooleanField(default=True, verbose_name='действителен')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email клиента')),
                ('is_active', models.BooleanField(default=True, verbose_name='действителен')),
                ('spammer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spammer_in_client', to='spammer.spammer', verbose_name='ФИО менеджера')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]