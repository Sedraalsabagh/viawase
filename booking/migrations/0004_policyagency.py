# Generated by Django 5.0.3 on 2024-05-01 07:32

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_delete_viawisepolicy'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifiable', models.BooleanField()),
                ('modify_period', models.DurationField(default=datetime.timedelta(0))),
                ('cancellable', models.BooleanField()),
                ('cancel_period', models.DurationField(default=datetime.timedelta(0))),
                ('cancel_without_payment', models.DurationField(default=datetime.timedelta(0))),
                ('cancellation_discount_amount', models.DecimalField(decimal_places=5, default=1, max_digits=15)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]