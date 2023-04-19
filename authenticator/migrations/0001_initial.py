# Generated by Django 4.2 on 2023-04-19 01:48

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
            name='PasswordStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_exhausted', models.DateTimeField(blank=True)),
                ('usage_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=30)),
                ('verified', models.BooleanField(default=False)),
                ('date_verified', models.DateTimeField(blank=True)),
                ('date_token_generated', models.DateTimeField(auto_now_add=True)),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_used_login', to='authenticator.passwordstorage')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_on_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usage_Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_used_owner', to='authenticator.registerclient')),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_involved', to='authenticator.passwordstorage')),
                ('usage_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_count', to='authenticator.passwordstorage')),
            ],
        ),
        migrations.AddField(
            model_name='passwordstorage',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_owner', to='authenticator.registerclient'),
        ),
        migrations.CreateModel(
            name='Password_log_on_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='abc@efg.com', max_length=254)),
                ('full_name', models.CharField(max_length=40)),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_patient_used', to='authenticator.passwordstorage')),
            ],
        ),
    ]
