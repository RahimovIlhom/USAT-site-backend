# Generated by Django 5.0.4 on 2024-10-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(blank=True, null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Question'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Answer'),
        ),
    ]
