# Generated by Django 2.0.7 on 2018-07-13 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0002_bankaccounts_client_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankbranch',
            options={'verbose_name_plural': 'BankBranch'},
        ),
        migrations.AlterModelOptions(
            name='otherbanks',
            options={'verbose_name_plural': 'OtherBanks'},
        ),
    ]
