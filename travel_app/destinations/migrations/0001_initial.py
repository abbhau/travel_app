# Generated by Django 5.0.3 on 2024-03-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('best_time_to_visit', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Beach', 'Beach'), ('Mountain', 'Mountain'), ('City', 'City'), ('Historical', 'Historical')], max_length=100)),
                ('image_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
