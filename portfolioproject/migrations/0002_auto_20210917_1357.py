# Generated by Django 3.2.5 on 2021-09-17 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioproject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='cemail',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='cmessage',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='cname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='csubject',
        ),
    ]
