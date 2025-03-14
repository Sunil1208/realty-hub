from django.contrib import admin

from apps.enquiries.models import Enquiry


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "subject", "message"]
    list_filter = ["email", "phone_number"]


admin.site.register(Enquiry, EnquiryAdmin)
