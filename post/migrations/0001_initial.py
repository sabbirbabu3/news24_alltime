# Generated by Django 5.0.1 on 2024-02-27 19:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('category', models.CharField(choices=[('Latest', 'Latest'), ('Politics', 'Politics'), ('Crime', 'Crime'), ('Opinion', 'Opinion'), ('Business', 'Business'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Jobs', 'Jobs'), ('Tech', 'Tech')], max_length=100)),
                ('publishing_time', models.DateTimeField(auto_now_add=True)),
                ('ratings', models.CharField(choices=[('one', '*'), ('two', '* *'), ('three', '* * *'), ('four', '* * * *')], max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
