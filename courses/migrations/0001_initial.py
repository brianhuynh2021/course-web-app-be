# Generated by Django 4.2.20 on 2025-04-03 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('length', models.IntegerField(help_text='Duration in minutes')),
                ('description', models.TextField()),
                ('cost', models.CharField(max_length=20)),
                ('thumbnail', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
