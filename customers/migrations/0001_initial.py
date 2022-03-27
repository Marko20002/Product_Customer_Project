# Generated by Django 2.0.7 on 2022-03-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('credit_card', models.CharField(max_length=16)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100)),
                ('number_of_adress', models.IntegerField()),
                ('Postal_code', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('country_name', models.CharField(max_length=100)),
            ],
        ),
    ]