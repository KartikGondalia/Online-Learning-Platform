# Generated by Django 2.2 on 2020-01-28 10:46

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
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=500)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('data', models.CharField(blank=True, max_length=1000)),
                ('image', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
