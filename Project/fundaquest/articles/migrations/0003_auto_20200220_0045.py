# Generated by Django 3.0.1 on 2020-02-19 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20200209_1201'),
        ('users', '0011_teacher_image'),
        ('articles', '0002_auto_20200129_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='static')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Teacher')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.Topic')),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]