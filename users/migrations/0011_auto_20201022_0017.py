# Generated by Django 3.0 on 2020-10-22 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_notificaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='barrio',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='departamento',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
