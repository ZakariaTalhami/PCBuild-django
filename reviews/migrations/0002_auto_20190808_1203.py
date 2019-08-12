# Generated by Django 2.2.3 on 2019-08-08 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.Part'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.Part'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('part', 'owner')},
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('part', 'owner')},
        ),
    ]