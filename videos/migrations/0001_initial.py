# Generated by Django 3.0.7 on 2020-06-17 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1000)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]