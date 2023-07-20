# Generated by Django 4.2.2 on 2023-07-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_possition', models.TextField()),
                ('starte_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_current', models.BooleanField()),
                ('address', models.TextField()),
                ('job_description', models.TextField()),
                ('company_name', models.TextField()),
            ],
        ),
    ]
