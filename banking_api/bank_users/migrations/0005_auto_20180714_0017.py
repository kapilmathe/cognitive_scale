# Generated by Django 2.0.7 on 2018-07-14 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0003_auto_20180713_1957'),
        ('bank_users', '0004_auto_20180713_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otherbankuserinfo',
            name='other_bank_id',
        ),
        migrations.RemoveField(
            model_name='userbeneficiaries',
            name='beneficiary_id',
        ),
        migrations.AddField(
            model_name='userbeneficiaries',
            name='other_bank_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bank_accounts.OtherBanks'),
        ),
        migrations.DeleteModel(
            name='OtherBankUserInfo',
        ),
    ]
