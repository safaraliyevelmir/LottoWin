from django.contrib import admin

from .models import AboutUs, FaqImage, Index, Join, JoinTitle, Country, Faq, RecentWinner, Service, Visitors



class FaqAdmin(admin.ModelAdmin):
    list_display = ['question','answer']



class JoinAdmin(admin.ModelAdmin):
    list_display = ['title','number']
    


admin.site.register(JoinTitle)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name','phone_code']


admin.site.register(Index)
admin.site.register(Join,JoinAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(AboutUs)
admin.site.register(Service)
admin.site.register(FaqImage)
admin.site.register(Visitors)
admin.site.register(RecentWinner)