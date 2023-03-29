from django.contrib import admin

from preview_app.models import Conference, Salle, Session, Intervenant, InterPresent, Presentation, Jour

# Register your models here.


admin.site.register([Conference, Jour, Salle, Session, Intervenant, InterPresent, Presentation])
