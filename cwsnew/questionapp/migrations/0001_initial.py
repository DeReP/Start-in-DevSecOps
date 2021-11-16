# Generated by Django 3.1.7 on 2021-10-14 07:02

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст карточки')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='card_img/', verbose_name='Картинка карточки')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.topic', verbose_name='Тема теста')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание вопроса')),
                ('topic', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='mainapp.topic', verbose_name='Тема')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст ответа')),
                ('correct', models.BooleanField(default=False, verbose_name='Ответ верен?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionapp.question', verbose_name='относится к вопросу')),
            ],
        ),
    ]
