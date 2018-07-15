# Generated by Django 2.0.7 on 2018-07-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionsDeposit',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_no', models.CharField(max_length=13)),
                ('transaction_info', models.CharField(max_length=1024)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsDepositHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_id', models.BigIntegerField()),
                ('account_no', models.CharField(max_length=13)),
                ('transaction_info', models.CharField(max_length=1024)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsWithdraw',
            fields=[
                ('transaction_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('account_no', models.CharField(max_length=13)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('transaction_info', models.CharField(max_length=1024)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionsWithdrawHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_id', models.BigIntegerField()),
                ('account_no', models.CharField(max_length=13)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=19)),
                ('transaction_info', models.CharField(max_length=1024)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
