# Generated by Django 4.2.1 on 2023-06-18 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAuthTokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=1500, verbose_name='Access token')),
                ('id_token', models.CharField(max_length=500, verbose_name='Id token')),
                ('expires_in', models.IntegerField(verbose_name='Expires in')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'OAuth токен',
                'verbose_name_plural': 'OAuth токены',
            },
        ),
    ]
