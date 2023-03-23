# Generated by Django 4.1.7 on 2023-03-23 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_password', models.CharField(max_length=15)),
                ('usage_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordLog_on_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=40)),
                ('age', models.DateField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_location', models.CharField(max_length=50)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PassWordSafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_count', models.PositiveIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_registered_password', to='authenticator.registerclient')),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_saved', to='authenticator.generatedpassword')),
            ],
        ),
        migrations.AddField(
            model_name='generatedpassword',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticator.registerclient'),
        ),
        migrations.AddField(
            model_name='generatedpassword',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_username', to='authenticator.registerclient'),
        ),
    ]
