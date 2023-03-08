"""
Module containing functions related to obtaining page context.
Functions:
- get_common_context: gets the common page context used across multiple pages of the site.
- get_page_context: gets the page context with the current request taken into account.
"""
from .forms import SubscriptionForm, ContactUsForm, FastBookingForm
from .models import Hiro, MenuItem, Servise, Team, Testimonial, About, Contacts


def get_common_context():
    """
    Gets the common page context used across multiple pages of the site.
    :return:
    """
    return {
        'slider': Hiro.objects.get(id=1),
        'menu_brk': MenuItem.objects.filter(type__exact='BRK')[0:8],
        'menu_lun': MenuItem.objects.filter(type__exact='LUN')[0:8],
        'menu_din': MenuItem.objects.filter(type__exact='DIN')[0:8],
        'servise': Servise.objects.get(id=1),
        'team': Team.objects.all().order_by('?')[:6],
        'testimonial': Testimonial.objects.filter(is_visible=True),
        'about': About.objects.get(id=1),
        'contacts': Contacts.objects.get(id=1),
        'contact_us': ContactUsForm(),
        'fast_booking': FastBookingForm(),
        'subscription': SubscriptionForm(),

    }


def get_page_context(request):
    """
    Gets the page context with the current request taken into account.
    Args:
    - request: HttpRequest object.
    Returns:
    - tuple of two elements:
        - dictionary containing data specific to the current request:
            'user_manager': True if the user is in the 'manager' group, False otherwise.
            'user_auth': True if the user is authenticated, False otherwise.
        - dictionary containing the common page context obtained from the get_common_context function.
    """
    data = {
        'user_manager': request.user.groups.filter(name='manager').exists(),
        'user_auth': request.user.is_authenticated,
    }
    context = get_common_context()
    data.update(context)
    return data