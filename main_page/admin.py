from django.contrib import admin
from main_page.models import Hiro, MenuItem, Servise, Testimonial, Team, About, Contacts, Subscription, ContactUs,\
    FastBooking


@admin.register(Hiro)
class HiroAdmin(admin.ModelAdmin):
    model = Hiro
    list_editable = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'back_image']
    list_display = ['title', 'position', 'image', 'is_visible', 'h_1', 'desc', 'back_image']
    list_display_links = None


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    model = MenuItem
    list_editable = ['title', 'position', 'image', 'is_visible', 'type', 'desc', 'price']
    list_display = ['title', 'position', 'image', 'is_visible', 'type', 'desc', 'price']
    list_display_links = None


@admin.register(Servise)
class ServiseAdmin(admin.ModelAdmin):
    model = Servise
    list_editable = ['h_5', 'h_1', 'title_1', 'desc_1', 'title_2', 'desc_2', 'title_3', 'desc_3', 'title_4', 'desc_4', 'position', 'is_visible']
    list_display = ['h_5', 'h_1', 'title_1', 'desc_1', 'title_2', 'desc_2', 'title_3', 'desc_3', 'title_4', 'desc_4', 'position', 'is_visible']
    list_display_links = None


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image', 'desc']
    list_display_links = None


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_editable = ['name', 'position', 'is_visible', 'profession', 'image']
    list_display = ['name', 'position', 'is_visible', 'profession', 'image']
    list_display_links = None


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    model = About
    list_editable = ['desc_1', 'desc_2', 'is_visible', 'experience', 'cook', 'img_1', 'img_2', 'img_3', 'img_4']
    list_display = ['desc_1', 'desc_2', 'is_visible', 'experience', 'cook', 'img_1', 'img_2', 'img_3', 'img_4']
    list_display_links = None


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_editable = ['address', 'phone', 'email_booking', 'email_general', 'email_technical', 'day_open',
                     'hours_of_work', 'weekend_work', 'weekend_hours_of_work', 'twi_url', 'fb_url', 'youtube_url', 'in_url']
    list_display = ['address', 'phone', 'email_booking', 'email_general', 'email_technical', 'day_open',
                    'hours_of_work', 'weekend_work', 'weekend_hours_of_work', 'twi_url', 'fb_url', 'youtube_url', 'in_url']
    list_display_links = None


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_editable = ['email', 'is_processed']
    list_display = ['email', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_editable = ['name', 'email', 'subject', 'message', 'is_processed']
    list_display = ['name', 'email', 'subject', 'message', 'date', 'date_processing', 'is_processed']
    list_display_links = None


@admin.register(FastBooking)
class FastBookingAdmin(admin.ModelAdmin):
    model = FastBooking
    list_editable = ['email', 'reservation_date', 'number_of_people', 'message', 'is_processed']
    list_display = ['name', 'email', 'reservation_date', 'number_of_people', 'message', 'date',
                    'date_processing', 'is_processed']


