from django.contrib import admin
from .models import Account, Samvaad, EmotionalIntelligenceWorkshop
from .models.user import User


# Register your models here.
class CustomAccount(admin.ModelAdmin):
    model = Account
    list_display = ('Mobile_Number', 'Whatsapp_Number', 'Organisation', 'Publicity')


admin.site.register(Account, CustomAccount)
admin.site.register(Samvaad)
admin.site.register(EmotionalIntelligenceWorkshop)
admin.site.register(User)
