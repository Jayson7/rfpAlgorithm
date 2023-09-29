# Generated by Django 3.2 on 2023-09-28 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('bmi', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('token', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=40)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease', models.CharField(max_length=100)),
                ('user_diagnosed', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Disease_result',
            fields=[
                ('disease', models.CharField(max_length=30)),
                ('mom_full_name', models.CharField(max_length=20)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('point', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=20, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mom_data',
            fields=[
                ('full_name', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('device_token', models.CharField(max_length=100)),
                ('app_password', models.CharField(max_length=100)),
                ('client_reference', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsSpanish',
            fields=[
                ('question', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Referal',
            fields=[
                ('token', models.CharField(max_length=30)),
                ('patient', models.CharField(max_length=40)),
                ('answer', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Result_owner',
            fields=[
                ('full_name', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=20)),
                ('app_password', models.CharField(max_length=20)),
                ('browser', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=50)),
                ('user_profile', models.CharField(max_length=20)),
                ('auth_password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSpanish',
            fields=[
                ('answer', models.CharField(max_length=200, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_ask_spanish', to='apps.questionsspanish')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer', models.CharField(max_length=200, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_to_ask', to='apps.questions')),
            ],
        ),
    ]
