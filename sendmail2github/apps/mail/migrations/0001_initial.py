# Generated by Django 3.1.6 on 2021-06-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('githubIssueNumber', models.IntegerField(db_index=True)),
                ('mailMessageId', models.CharField(max_length=1024)),
                ('mailSenderAddress', models.CharField(max_length=1024)),
                ('mailTitle', models.CharField(max_length=1024)),
            ],
        ),
    ]
