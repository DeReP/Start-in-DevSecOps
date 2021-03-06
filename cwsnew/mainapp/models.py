from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField
from django.conf import settings

class Topic(models.Model):
     topic = models.CharField(max_length=128, verbose_name="Тема")
     def __str__(self):
        return self.topic


class Card(models.Model):
    image = ThumbnailerImageField(
        upload_to='card_img/', verbose_name="Картинка карточки", blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    text = models.CharField(max_length=512, verbose_name="Текст карточки")
    order = models.IntegerField(verbose_name="Порядковый номер карточки", default=1000)
    topic = models.OneToOneField("Topic", on_delete=models.CASCADE)   

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Education', args=[self.topic_id])

class ContentCard(models.Model):
    text = RichTextUploadingField(verbose_name='Содержание карточки')
    topic = models.ForeignKey("Topic", on_delete=models.PROTECT, default=0)
    order = models.IntegerField(verbose_name="Порядковый номер карточки", default=1000)
    label = models.CharField(
        max_length=32, verbose_name="Обозначение карточки при пагинации", default=order)
    
    def __str__(self):
        return "{} | {} | {} ...".format(self.topic, self.order, self.text[:100])


class Comment(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, verbose_name="Тема")
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(unique=False)
    date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s: %s..." % (self.user.username, self.content[:50])
