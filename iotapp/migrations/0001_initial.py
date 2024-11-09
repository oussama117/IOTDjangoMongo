# Generated by Django 5.1.3 on 2024-11-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cheepNecklace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNecklace', models.CharField(max_length=60)),
                ('acceleration', models.FloatField()),
                ('gyroscope', models.FloatField()),
                ('pulse', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('time', models.IntegerField()),
            ],
        ),
    ]