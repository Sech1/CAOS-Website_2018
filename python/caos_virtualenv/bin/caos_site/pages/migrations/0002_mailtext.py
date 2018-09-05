# Generated by Django 2.1 on 2018-09-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000, verbose_name='Subject')),
                ('header', models.CharField(max_length=1000, verbose_name='Header')),
                ('message', models.CharField(max_length=25000, verbose_name='Message')),
                ('send_it', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Emails to send',
                'verbose_name_plural': 'Emails to send',
            },
        ),
    ]
