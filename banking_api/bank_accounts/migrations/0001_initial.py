# Generated by Django 2.0.7 on 2018-07-13 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccontNumberGenerator',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('account_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_no', models.CharField(db_index=True, max_length=13, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='BankBranch',
            fields=[
                ('branch_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('branch_code', models.CharField(db_index=True, max_length=10, unique=True)),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_address', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OtherBanks',
            fields=[
                ('bank_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_branch_code', models.CharField(db_index=True, max_length=10, unique=True)),
                ('bank_branch_info', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bankaccounts',
            name='bank_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank_accounts.BankBranch'),
        ),
    ]
