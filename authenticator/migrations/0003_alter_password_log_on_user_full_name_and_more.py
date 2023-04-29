# Generated by Django 4.2 on 2023-04-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0002_alter_userlogintoken_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password_log_on_user',
            name='full_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='password_log_on_user',
            name='password',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='password_patient_used', to='authenticator.passwordstorage'),
        ),
    ]
