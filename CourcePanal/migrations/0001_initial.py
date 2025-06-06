# Generated by Django 5.1.6 on 2025-04-12 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='courses/')),
                ('Name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=400)),
                ('duration', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
                ('By', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_file', models.FileField(upload_to='certificates/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='CourcePanal.cource')),
            ],
        ),
        migrations.AddField(
            model_name='cource',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cource', to='CourcePanal.lang'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.CharField(max_length=300)),
                ('Name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('Cource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lesson', to='CourcePanal.cource')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Exam', to='CourcePanal.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Done_Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DoneLessons', to=settings.AUTH_USER_MODEL)),
                ('Done_Lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DoneLessons', to='CourcePanal.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Q',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q', models.CharField(max_length=2000)),
                ('answer1', models.CharField(max_length=2000)),
                ('answer2', models.CharField(max_length=2000)),
                ('answer3', models.CharField(max_length=2000)),
                ('TrueAnswer', models.CharField(max_length=2000)),
                ('Exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Q', to='CourcePanal.exam')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Certificate_Name', models.CharField(max_length=255)),
                ('Done_Cource', models.BooleanField(default=False)),
                ('Done_Lesson', models.BooleanField(default=False)),
                ('Done_Exam', models.BooleanField(default=False)),
                ('Cource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscribe', to='CourcePanal.cource')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subscribe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
