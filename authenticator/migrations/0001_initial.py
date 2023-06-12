# Generated by Django 3.2 on 2023-06-12 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20)),
                ('auth_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_exhausted', models.DateTimeField(blank=True, null=True)),
                ('usage_count', models.PositiveIntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_owner', to='authenticator.registerclient')),
            ],
        ),
    ]
