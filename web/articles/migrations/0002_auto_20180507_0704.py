# Generated by Django 2.0.5 on 2018-05-07 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_articles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]