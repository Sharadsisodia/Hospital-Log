from django.contrib import admin
from formlogin.models import patient,doctor,Category, imagePost, appointmentData

# Register your models here.
class pateintAdmin(admin.ModelAdmin):
    list_display=('p_Firstname','p_Lastname','p_Picture','p_Username','p_EmailId','p_Password','p_AddressLi','p_City','p_State','p_Pincode')

class doctorAdmin(admin.ModelAdmin):
    list_display=('d_Firstname','d_Lastname','d_Picture','d_Username','d_EmailId','d_Password','d_AddressLi','d_City','d_State','d_Pincode')

class imagePostAdmin(admin.ModelAdmin):
    list_display=('iTitle','iImage','iCategory','iSummary','iContent')

class CategoryAdmin(admin.ModelAdmin):
    # list_display=('title','image','summary')
    pass

class appointmentDataAdmin(admin.ModelAdmin):
    list_display=("ap_username","ap_specilist","ap_date","ap_startTime","ap_endTime")


admin.site.register(patient,pateintAdmin)
admin.site.register(doctor,doctorAdmin)
admin.site.register(imagePost,imagePostAdmin)
# admin.site.register(Category,CategoryAdmin)
admin.site.register(appointmentData,appointmentDataAdmin)


