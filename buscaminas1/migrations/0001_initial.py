# Generated by Django 4.2.6 on 2023-10-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension_x', models.IntegerField()),
                ('dimension_y', models.IntegerField()),
            ],
        ),
    ]
