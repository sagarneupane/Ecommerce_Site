from django.contrib import admin
from dynamictemplate.models import *


# Register your models here.

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ["id","logo_name","logo_image","active_status","date_added","date_edited"]
    
@admin.register(ContactAddress)
class ContactAddressAdmin(admin.ModelAdmin):
    list_display = ["company_name",
                    "address_line_1","address_line_2",
                    "contact_1","contact_2",
                    "email_1","email_2",
                    "google_embedding_link",
                    "active_status","date_added","date_edited"]


@admin.register(CarosulData)
class CarosulDataAdmin(admin.ModelAdmin):
    list_display = ["headline","description","date_added","date_edited","headline_image","special_offer","active_status","offer_discount"]
    

admin.sites.AdminSite.site_title = "NEUPANE FANCY"

admin.sites.AdminSite.site_header = "NFS ADMIN"

