# Generated by Django 5.0.4 on 2024-10-03 07:06

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
            name='EduDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Edu direction',
                'verbose_name_plural': 'Edu directions',
            },
        ),
        migrations.CreateModel(
            name='EduType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Edu type',
                'verbose_name_plural': 'Edu types',
            },
        ),
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('study_duration', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Study duration')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu_programs', to='education.edudirection', verbose_name='Direction')),
                ('edu_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edu_programs', to='education.edutype', verbose_name='Edu type')),
            ],
            options={
                'verbose_name': 'Edu program',
                'verbose_name_plural': 'Edu programs',
            },
        ),
    ]
