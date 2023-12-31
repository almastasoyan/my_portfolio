# Generated by Django 4.2.2 on 2023-07-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_alter_message_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
