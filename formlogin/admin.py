from django.contrib import admin
from formlogin.models import patient,doctor,Category, imagePost, draft

# Register your models here.
class pateintAdmin(admin.ModelAdmin):
    list_display=('p_Firstname','p_Lastname','p_Picture','p_Username','p_EmailId','p_Password','p_AddressLi','p_City','p_State','p_Pincode')

class doctorAdmin(admin.ModelAdmin):
    list_display=('d_Firstname','d_Lastname','d_Picture','d_Username','d_EmailId','d_Password','d_AddressLi','d_City','d_State','d_Pincode')

class imagePostAdmin(admin.ModelAdmin):
    list_display=('iTitle','iImage','iCategory','iSummary','iContent')

class draftAdmin(admin.ModelAdmin):
    list_display=('dTitle','dImage','dCategory','dSummary','dContent')

class CategoryAdmin(admin.ModelAdmin):
    # list_display=('title','image','summary')
    pass

admin.site.register(patient,pateintAdmin)
admin.site.register(doctor,doctorAdmin)
admin.site.register(imagePost,imagePostAdmin)
admin.site.register(draft,draftAdmin)
# admin.site.register(Category,CategoryAdmin)


