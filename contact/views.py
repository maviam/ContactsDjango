from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q

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

# Search for a contact
def search(request):
    # search_value = request.GET
    # print(search_value)
    search_value = request.GET.get('q','').strip()
    
    if search_value == "":
        return redirect("contact:index")
    
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)).order_by("-id")[0:10]
    context = {
        'contacts': contacts,
        'page_title': 'Contacts'
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
        'page_title': f"{single_contact.first_name} {single_contact.last_name}"
    }
    return render(
        request,
        'contact/contact.html',
        context
    )