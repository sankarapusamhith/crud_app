# Generated by Django 4.1.7 on 2023-03-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=3, verbose_name='Age')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
            ],
        ),
    ]
