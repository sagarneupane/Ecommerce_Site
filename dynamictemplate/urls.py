from django.urls import path
import dynamictemplate.views as vi

urlpatterns = [
    path("",vi.dashboard,name="dashboard"),
    path("login/",vi.signin,name="login"),
    path("register/",vi.signup,name="register"),
    path("checkout/",vi.checkout,name="checkout"),
    path("viewcard/",vi.view_cart,name="viewcard"),
    path("blog/",vi.blog,name="blog"),
    path("blog-details/",vi.blog_details,name="blog-details"),
    path("contact/",vi.contact,name="contact"),
    path("faq/",vi.faq,name="faq"),
    path("shop/",vi.shop,name="shop"),
    
]
