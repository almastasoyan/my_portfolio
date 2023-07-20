# Generated by Django 4.2.2 on 2023-07-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0016_remove_personalinfo_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]