from django.db import models

STATUS_CHOICES = [
    ('published', 'Опубликовано'),
    ('archived', 'В архиве'),
]

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Содержание статьи', max_length=5000)   
    image = models.ImageField(upload_to='articles/', blank=True, verbose_name='Главное изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='published', verbose_name='Статус')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
