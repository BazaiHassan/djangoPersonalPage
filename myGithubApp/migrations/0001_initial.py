# Generated by Django 3.2.5 on 2022-09-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repository_name', models.CharField(max_length=80)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('repo_image', models.ImageField(blank=True, upload_to='images/repositories/')),
            ],
        ),
    ]
