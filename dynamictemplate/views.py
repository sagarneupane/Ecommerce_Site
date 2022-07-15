from django.shortcuts import render
from dynamictemplate.models import Logo,ContactAddress,CarosulData


Logo_details = Logo.objects.get(active_status=True)
Contact_details = ContactAddress.objects.get(active_status=True)


# Create your views here.
def dashboard(request):
    carasoul_items = None
    carasoul_data = CarosulData.objects.filter(active_status=True)
    if carasoul_data.exists():
        carasoul_items = carasoul_data
    
    context = {"logo_details":Logo_details,"contact":Contact_details,"carasoul_items":carasoul_items}
    return render(request,'main/hero.html',context)

def signin(request):
    return render(request,'main/signin.html',{"logo_details":Logo_details,"contact":Contact_details})

def signup(request):
    return render(request,'main/signup.html',{"logo_details":Logo_details,"contact":Contact_details})


def view_cart(request):
    return render(request,'main/viewcart.html',{"logo_details":Logo_details,"contact":Contact_details})


def checkout(request):
    return render(request,'main/checkout.html',{"logo_details":Logo_details,"contact":Contact_details})

def contact(request):

    return render(request,'main/contact.html',{"contact":Contact_details,"logo_details":Logo_details})

def faq(request):
    return render(request,'main/faq.html',{"logo_details":Logo_details,"contact":Contact_details})

def blog(request):
    return render(request,'main/blog.html',{"logo_details":Logo_details,"contact":Contact_details})

def blog_details(request):
    return render(request, 'main/blog-details.html',{"logo_details":Logo_details,"contact":Contact_details})

def shop(request):
    return render(request,'main/shop.html',{"logo_details":Logo_details,"contact":Contact_details})