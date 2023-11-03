from django.db import models
from pytils.translit import slugify

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='posts/', verbose_name='превью', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_image = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ('-date_of_creation',)
