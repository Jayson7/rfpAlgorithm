# Generated by Django 3.2 on 2023-06-03 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('user_diagnosed', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Disease_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=30)),
                ('mom_full_name', models.CharField(max_length=20)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('point', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mom_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('device_token', models.CharField(max_length=100)),
                ('app_password', models.CharField(max_length=100)),
                ('client_reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsSpanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Result_owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=20)),
                ('app_password', models.CharField(max_length=20)),
                ('browser', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=50)),
                ('user_profile', models.CharField(max_length=20)),
                ('auth_password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSpanish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_ask_spanish', to='apps.questionsspanish')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=200, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_ask', to='apps.questions')),
            ],
        ),
    ]
