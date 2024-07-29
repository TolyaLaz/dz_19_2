from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    slug = models.CharField(max_length=255, verbose_name='slug')
    text = models.TextField(verbose_name=_('Текст'))
    preview = models.ImageField(upload_to='posts/', verbose_name=_('Превью'), blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    is_published = models.BooleanField(default=False, verbose_name=_('Опубликовано'))
    views_count = models.IntegerField(default=0, verbose_name=_('Количество просмотров'))

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return self.title
