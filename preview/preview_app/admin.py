from django.contrib import admin

from preview_app.models import Conference, Salle, Session, Intervenant, InterPresent, Presentation

# Register your models here.


admin.site.register(Conference)
admin.site.register(Salle)
admin.site.register(Session)
admin.site.register(Intervenant)
admin.site.register(Presentation)
admin.site.register(InterPresent)
