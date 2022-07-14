from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'main/hero.html')

def signin(request):
    return render(request,'main/signin.html')

def signup(request):
    return render(request,'main/signup.html')


def view_cart(request):
    return render(request,'main/viewcart.html')


def checkout(request):
    return render(request,'main/checkout.html')

def contact(request):
    return render(request,'main/contact.html')

def faq(request):
    return render(request,'main/faq.html')

def blog(request):
    return render(request,'main/blog.html')

def blog_details(request):
    return render(request, 'main/blog-details.html')

def shop(request):
    return render(request,'main/shop.html')