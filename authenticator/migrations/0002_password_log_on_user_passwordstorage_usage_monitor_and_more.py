# Generated by Django 4.1.7 on 2023-03-25 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password_log_on_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=40)),
                ('age', models.DateField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=12)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('date_exhausted', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_owner', to='authenticator.registerclient')),
            ],
        ),
        migrations.CreateModel(
            name='Usage_Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_count', models.PositiveIntegerField(default=0)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_used_owner', to='authenticator.registerclient')),
                ('password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_involved', to='authenticator.passwordstorage')),
            ],
        ),
        migrations.DeleteModel(
            name='PasswordLog_on_User',
        ),
        migrations.DeleteModel(
            name='PassWordSafe',
        ),
        migrations.AlterField(
            model_name='generatedpassword',
            name='password',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_expected', to='authenticator.passwordstorage'),
        ),
        migrations.AlterField(
            model_name='generatedpassword',
            name='usage_count',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_count', to='authenticator.usage_monitor'),
        ),
    ]
