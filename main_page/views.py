from django.shortcuts import render, redirect
from .context_data import get_common_context, get_page_context
from .forms import SubscriptionForm, ContactUsForm, FastBookingForm
from .models import Subscription, ContactUs
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


def handle_post_request(request):
    print('fast_booking')

    fast_booking = FastBookingForm(request.POST)
    subscription = SubscriptionForm(request.POST)
    contact_us = ContactUsForm(request.POST)

    if fast_booking.is_valid():
        fast_booking.save()
        return redirect('/')
    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')


def index(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'index.html', context=data)

def about(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'about.html', context=data)

def menu(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'menu.html', context=data)

def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'contact.html', context=data)


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_manager(request, pk):
    Subscription.objects.filter(pk=pk).update(is_processed=True)
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('main_page:manager_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def manager_list(request):
    subscription_viev_manager = Subscription.objects.filter(is_processed=False)
    contact_us_viev_manager = ContactUs.objects.filter(is_processed=False)

    data = {
        'subscription_viev_manager': subscription_viev_manager,
        'contact_us_viev_manager': contact_us_viev_manager,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'manager.html', context=data)