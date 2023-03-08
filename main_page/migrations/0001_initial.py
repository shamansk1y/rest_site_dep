# Generated by Django 4.1.7 on 2023-03-08 17:13

from django.db import migrations, models
import main_page.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_1', models.TextField(max_length=500, verbose_name='Опис 1')),
                ('desc_2', models.TextField(max_length=500, verbose_name='Опис 2')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('experience', models.SmallIntegerField(verbose_name='Роки роботи')),
                ('cook', models.SmallIntegerField(verbose_name='Кількість поварів')),
                ('img_1', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення 1')),
                ('img_2', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення 2')),
                ('img_3', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення 3')),
                ('img_4', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення 4')),
            ],
            options={
                'verbose_name_plural': 'Про нас',
                'ordering': ('desc_1',),
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='Адреса')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('email_booking', models.CharField(max_length=50, verbose_name='Пошта Booking')),
                ('email_general', models.CharField(max_length=50, verbose_name='Пошта General')),
                ('email_technical', models.CharField(max_length=50, verbose_name='Пошта Technical')),
                ('day_open', models.CharField(max_length=50, verbose_name='Робочі дні')),
                ('hours_of_work', models.CharField(max_length=50, verbose_name='Робочі години')),
                ('weekend_work', models.CharField(max_length=50, verbose_name='Робота в вихідні')),
                ('weekend_hours_of_work', models.CharField(max_length=50, verbose_name='Робочі години в вихідні')),
                ('twi_url', models.URLField(blank=True, default='https://twitter.com/', verbose_name='Посилання на twitter')),
                ('fb_url', models.URLField(blank=True, default='https://www.facebook.com/', verbose_name='Посилання на facebook')),
                ('youtube_url', models.URLField(blank=True, default='https://www.youtube.com/', verbose_name='Посилання на youtube')),
                ('in_url', models.URLField(blank=True, default='https://www.instagram.com/', verbose_name='Посилання на instagram')),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'ordering': ('address',),
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, max_length=250)),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': "Зворотній зв'язок",
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='FastBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('reservation_date', models.DateTimeField()),
                ('number_of_people', models.IntegerField(choices=[(1, 'people 1'), (2, 'people 2'), (3, 'people 3'), (4, 'people 4'), (5, 'people 5'), (6, 'people 6')])),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Швидке бронювання',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Hiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва слайду')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('back_image', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Фонове зображення')),
                ('image', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('h_1', models.CharField(blank=True, max_length=250, verbose_name='Заголовок')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Опис')),
            ],
            options={
                'verbose_name_plural': 'Слайдер',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва страви')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('image', models.ImageField(upload_to=main_page.utils.get_file_name, verbose_name='Зображення')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('type', models.CharField(choices=[('BRK', 'Breakfast'), ('LUN', 'Launch'), ('DIN', 'Dinner')], default='BRK', max_length=3, verbose_name='Тип')),
            ],
            options={
                'verbose_name_plural': 'Страви',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Servise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h_5', models.CharField(default='text', max_length=50, verbose_name='Назва розділу')),
                ('h_1', models.CharField(default='text', max_length=50, verbose_name='Текст розділу')),
                ('title_1', models.CharField(default='text', max_length=50, verbose_name='Назва послуги 1')),
                ('desc_1', models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 1')),
                ('title_2', models.CharField(default='text', max_length=50, verbose_name='Назва послуги 2')),
                ('desc_2', models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 2')),
                ('title_3', models.CharField(default='text', max_length=50, verbose_name='Назва послуги 3')),
                ('desc_3', models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 3')),
                ('title_4', models.CharField(default='text', max_length=50, verbose_name='Назва послуги 4')),
                ('desc_4', models.TextField(blank=True, default='text', max_length=500, verbose_name='Опис 4')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
            ],
            options={
                'verbose_name_plural': 'Послуги',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processing', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Підписка на email розсилку',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Повне ім'я")),
                ('profession', models.TextField(max_length=50, verbose_name='Посада')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('image', models.ImageField(blank=True, upload_to=main_page.utils.get_file_name, verbose_name='Фото')),
                ('twi_url', models.URLField(blank=True, default='https://twitter.com/', verbose_name='Посилання на twitter')),
                ('fb_url', models.URLField(blank=True, default='https://www.facebook.com/', verbose_name='Посилання на facebook')),
                ('in_url', models.URLField(blank=True, default='https://www.instagram.com/', verbose_name='Посилання на instagram')),
            ],
            options={
                'verbose_name_plural': 'Наша команда',
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Повне ім'я")),
                ('profession', models.TextField(max_length=50, verbose_name='Посада')),
                ('position', models.SmallIntegerField(unique=True, verbose_name='Позиція')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимість')),
                ('image', models.ImageField(blank=True, upload_to=main_page.utils.get_file_name, verbose_name='Фото')),
                ('desc', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
            ],
            options={
                'verbose_name_plural': 'Відгуки',
                'ordering': ('position',),
            },
        ),
    ]