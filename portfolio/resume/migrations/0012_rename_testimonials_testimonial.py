# Generated by Django 4.2.2 on 2023-07-16 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_testimonials_experience_created_on_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]
