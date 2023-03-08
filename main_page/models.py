from django.db import models
from .utils import get_file_name


class Hiro(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    back_image = models.ImageField(upload_to=get_file_name, verbose_name="Фонове зображення")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class MenuItem(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва страви")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    TYPE = [
        ('BRK', 'Breakfast'),
        ('LUN', 'Launch'),
        ('DIN', 'Dinner'),
    ]

    type = models.CharField(choices=TYPE, max_length=3, default='BRK', verbose_name='Тип')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Страви'


class Servise(models.Model):

    h_5 = models.CharField(max_length=50, verbose_name="Назва розділу", default='text')
    h_1 = models.CharField(max_length=50, verbose_name="Текст розділу", default='text')
    title_1 = models.CharField(max_length=50, verbose_name="Назва послуги 1", default='text')
    desc_1 = models.TextField(max_length=500, blank=True, verbose_name="Опис 1", default='text')
    title_2 = models.CharField(max_length=50, verbose_name="Назва послуги 2", default='text')
    desc_2 = models.TextField(max_length=500, blank=True, verbose_name="Опис 2", default='text')
    title_3 = models.CharField(max_length=50, verbose_name="Назва послуги 3", default='text')
    desc_3 = models.TextField(max_length=500, blank=True, verbose_name="Опис 3", default='text')
    title_4 = models.CharField(max_length=50, verbose_name="Назва послуги 4", default='text')
    desc_4 = models.TextField(max_length=500, blank=True, verbose_name="Опис 4", default='text')
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")

    def __str__(self):
        return f'{self.h_5}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Послуги'


class Testimonial(models.Model):

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Відгуки'


class Team(models.Model):
    """
    A model representing a team member.
    Fields:
        - name (CharField): The full name of the team member.
        - profession (TextField): The job title or profession of the team member.
        - position (SmallIntegerField): The unique position of the team member within the team.
        - is_visible (BooleanField): Whether the team member should be visible on the website or not.
        - image (ImageField): An optional image of the team member.
        - desc (TextField): A brief description or bio of the team member.
        - image_clas (ImageField): An optional image of the team member's class.
        - twi_url (URLField): The team member's Twitter profile URL.
        - fb_url (URLField): The team member's Facebook profile URL.
        - in_url (URLField): The team member's Instagram profile URL.
    Methods:
        - __str__: Returns the full name of the team member.
    Meta:
        - ordering: Specifies the default ordering for the model's objects.
        - verbose_name_plural: A human-readable plural name for the model in the admin interface.
    """

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    twi_url = models.URLField(blank=True, verbose_name="Посилання на twitter", default='https://twitter.com/')
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.facebook.com/')
    in_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Наша команда'


class About(models.Model):

    desc_1 = models.TextField(max_length=500, verbose_name="Опис 1")
    desc_2 = models.TextField(max_length=500, verbose_name="Опис 2")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    experience = models.SmallIntegerField(verbose_name="Роки роботи")
    cook = models.SmallIntegerField(verbose_name="Кількість поварів")
    img_1 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення 1")
    img_2 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення 2")
    img_3 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення 3")
    img_4 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення 4")

    def __str__(self):
        return f'{self.desc_1}'

    class Meta:
        ordering = ('desc_1',)
        verbose_name_plural = 'Про нас'


class Contacts(models.Model):

    address = models.CharField(max_length=50, verbose_name="Адреса")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email_booking = models.CharField(max_length=50, verbose_name="Пошта Booking")
    email_general = models.CharField(max_length=50, verbose_name="Пошта General")
    email_technical = models.CharField(max_length=50, verbose_name="Пошта Technical")
    day_open = models.CharField(max_length=50, verbose_name="Робочі дні")
    hours_of_work = models.CharField(max_length=50, verbose_name="Робочі години")
    weekend_work = models.CharField(max_length=50, verbose_name="Робота в вихідні")
    weekend_hours_of_work = models.CharField(max_length=50, verbose_name="Робочі години в вихідні")
    twi_url = models.URLField(blank=True, verbose_name="Посилання на twitter", default='https://twitter.com/')
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.facebook.com/')
    youtube_url = models.URLField(blank=True, verbose_name="Посилання на youtube", default='https://www.youtube.com/')
    in_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')

    def __str__(self):
        return f'{self.address}'

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'Контакти'


class Subscription(models.Model):

    email = models.EmailField()
    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Підписка на email розсилку'


class ContactUs(models.Model):
    """
    Defines a model `ContactUs` that represents a contact form submission.
    Fields:
        - name: a CharField representing the name of the person submitting the form
        - email: an EmailField representing the email address of the person submitting the form
        - message: a TextField representing the message the person submitting the form wants to convey
        - subject: a CharField representing the subject of the message
        - date: a DateField representing the date when the form was submitted
        - date_processing: a DateField representing the date when the form was processed
        - is_processed: a BooleanField representing whether the form has been processed or not
    Methods:
        - __str__: returns a string representation of the model instance
    Meta:
        - ordering: a tuple that specifies the default ordering for instances of the model
        - verbose_name_plural: a string that specifies the plural name for the model in the admin interface
    """

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Зворотній зв'язок"


class FastBooking(models.Model):
    PEOPLE_CHOICES = (
        (1, 'people 1'),
        (2, 'people 2'),
        (3, 'people 3'),
        (4, 'people 4'),
        (5, 'people 5'),
        (6, 'people 6'),
    )

    name = models.CharField(max_length=50)
    email = models.EmailField()
    reservation_date = models.DateTimeField(blank=True)
    number_of_people = models.IntegerField(choices=PEOPLE_CHOICES)
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.reservation_date}: {self.email}'
    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Швидке бронювання'