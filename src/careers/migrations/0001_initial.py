# Generated by Django 5.0.2 on 2024-03-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.URLField(unique=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('title', models.IntegerField()),
                ('content', models.FloatField()),
            ],
            options={
                'verbose_name': 'career',
                'verbose_name_plural': 'careers',
                'ordering': ['id'],
            },
        ),
    ]
