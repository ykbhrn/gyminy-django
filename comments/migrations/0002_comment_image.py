# Generated by Django 3.0.7 on 2020-06-17 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='images.Image'),
        ),
    ]
