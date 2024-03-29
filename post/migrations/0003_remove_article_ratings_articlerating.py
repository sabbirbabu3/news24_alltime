# Generated by Django 5.0.1 on 2024-02-27 20:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_article_publishing_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='ratings',
        ),
        migrations.CreateModel(
            name='ArticleRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[('one', '*'), ('two', '* *'), ('three', '* * *'), ('four', '* * * *')])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='post.article')),
            ],
        ),
    ]
