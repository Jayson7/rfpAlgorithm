# Generated by Django 3.2 on 2023-05-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_exhausted', models.DateTimeField(blank=True, null=True)),
                ('usage_count', models.PositiveIntegerField(default=0)),
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
                ('auth_password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=30)),
                ('verified', models.BooleanField(default=False)),
                ('date_verified', models.DateTimeField(blank=True, null=True)),
                ('date_token_generated', models.DateTimeField(auto_now_add=True)),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_used_login', to='authenticator.passwordstorage')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_on_user', to='authenticator.registerclient')),
            ],
        ),
        migrations.CreateModel(
            name='StoreDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=300)),
                ('browser', models.CharField(max_length=300)),
                ('user_profile_token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_used', to='authenticator.userlogintoken')),
                ('username_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_owner_mum', to='authenticator.registerclient')),
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
