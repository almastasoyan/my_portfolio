# Generated by Django 4.2.2 on 2023-07-18 03:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0014_remove_profile_for_me_profile_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=50)),
                ('age', models.PositiveIntegerField(default=18, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(18)])),
                ('email', models.EmailField(max_length=254)),
                ('about_me', models.TextField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
