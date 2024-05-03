# Generated by Django 5.0.3 on 2024-05-02 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0022_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='destination_activity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='destination_climate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='destination_type',
            field=models.CharField(blank=True, choices=[('Business', 'Business'), ('Tourism', 'Tourism'), ('Education', 'Education'), ('Entertainment', 'Entertainment')], max_length=100, null=True),
        ),
    ]