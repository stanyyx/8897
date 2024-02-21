from django.db import models

class Themes(models.Model):
    themes = models.CharField(max_length=100, verbose_name='Тема')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    themes = models.ManyToManyField(Themes, through='relations', through_fields=('article', 'theme'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE)
    main = models.BooleanField(verbose_name='Главная Тема')
