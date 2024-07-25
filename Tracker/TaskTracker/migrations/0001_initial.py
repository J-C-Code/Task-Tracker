# Generated by Django 5.0.7 on 2024-07-24 17:21

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
            name='Task',
            fields=[
                ('task_name', models.CharField(max_length=30)),
                ('task_complete', models.BooleanField()),
                ('task_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('task_due', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]