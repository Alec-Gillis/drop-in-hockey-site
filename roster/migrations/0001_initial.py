# Generated by Django 4.1 on 2022-09-05 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('is_checked_in', models.BooleanField(default=False)),
                ('is_goalie', models.BooleanField(default=False)),
            ],
        ),
    ]
