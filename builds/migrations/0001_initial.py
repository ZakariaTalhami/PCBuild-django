# Generated by Django 2.2.3 on 2019-08-08 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PcBuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('cpu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parts.Cpu')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
