# Generated by Django 5.1.4 on 2025-01-06 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0004_alter_applogin_email_alter_applogin_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction_details',
            old_name='account_number',
            new_name='account_no',
        ),
        migrations.RenameField(
            model_name='transaction_details',
            old_name='my_account',
            new_name='my_account_id',
        ),
    ]
