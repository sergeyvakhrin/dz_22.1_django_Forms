from django.db import models

NULLABLE = {"null": True, "blank": True}

class Blog(models.Model):
    """ Класс для модели Блог """
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Введите заголовок")
    slug = models.CharField(max_length=100, verbose_name="Путь", unique=True)
    post = models.TextField(verbose_name="Статья", help_text="Введите текс")
    image = models.ImageField(upload_to="blog/", verbose_name="Фото", **NULLABLE, help_text="Загрузите фото")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ("title",)
