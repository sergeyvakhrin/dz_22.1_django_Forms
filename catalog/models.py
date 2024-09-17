from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    """ Класс для модели Категория """
    category_name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    category_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("category_name",)


class Product(models.Model):
    """ Класс для модели Продукт """
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите ниаменование продукта"
    )
    product_description = models.TextField(
        verbose_name="Описание продуктв",
        help_text="Введите описание продукта",
        **NULLABLE
    )
    product_image = models.ImageField(
        upload_to="product/",
        verbose_name="Фото",
        **NULLABLE,
        help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        **NULLABLE,
        related_name="Products"
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateTimeField(
        verbose_name="Дата создания", help_text="Введите дату создания", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения", help_text="Введите дату изменения", auto_now=True
    )

    def __str__(self):
        """ Строковое представление данных """
        return f"{self.product_name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("product_name",)


class Contact(models.Model):
    """ Класс для модели Контакты """
    name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="Введите имя"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон для связи",
        help_text="Введите телефон для связи",
    )
    message = models.TextField(
        verbose_name="Текст сообщения",
        help_text="Введите текст сообщения"
    )

    def __str__(self):
        """ Строковое представление данных """
        return f'{self.name}'

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("name",)

