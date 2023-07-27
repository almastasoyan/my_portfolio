# Generated by Django 4.2.2 on 2023-07-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0024_alter_sociallink_link_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
