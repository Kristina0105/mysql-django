# Generated by Django 5.0.2 on 2024-02-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialization', models.CharField(choices=[('Italian', 'Italian'), ('French', 'French'), ('Asian', 'Asian'), ('Family', 'Family'), ('Other', 'Other')], max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
