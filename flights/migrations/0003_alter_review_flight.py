# Generated by Django 5.0.3 on 2024-05-18 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_remove_flight_user_alter_review_flight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='flights.flight'),
        ),
    ]
