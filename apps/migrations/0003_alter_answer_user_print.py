# Generated by Django 3.2 on 2023-05-07 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
        ('apps', '0002_auto_20230507_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_print',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_in_question', to='authenticator.userlogintoken'),
        ),
    ]
