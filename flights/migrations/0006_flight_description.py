# Generated by Django 5.0.3 on 2024-05-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_review_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='description',
            field=models.TextField(blank=True, default='', max_length=2000, null=True),
        ),
    ]