# Generated by Django 4.2.2 on 2023-07-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_remove_sociallink_class_name_sociallink_icon_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='link_icon',
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='icon_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='link_name',
            field=models.CharField(max_length=100),
        ),
    ]