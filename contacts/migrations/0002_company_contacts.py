# Generated by Django 3.1 on 2020-09-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_phone', models.CharField(max_length=100)),
                ('company_email', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=100)),
            ],
        ),
    ]
