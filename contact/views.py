from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")[0:10]
    context = {
        'contacts': contacts,
        'page_title': 'Contacts List'
    }
    return render(
        request,
        'contact/index.html',
        context
    )


# See a specific contact
def contact(request, contact_id):
    single_contact = get_object_or_404(Contact.objects, id=contact_id, show=True)
    context = {
        'contact': single_contact,
        'page_title': f"Contact no. {contact_id}"
    }
    return render(
        request,
        'contact/contact.html',
        context
    )