# Generated by Django 5.1.3 on 2024-11-09 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cloudflare_id', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
