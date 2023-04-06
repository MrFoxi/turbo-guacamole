"""preview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from preview_app import views as preview_app_view
from conference import views as conference_view
from presentation import views as presentation_view
from planning import views as planning_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conference/', conference_view.index, name='conference'),
    path('presentation/', presentation_view.presentation, name='presentation'),
    # PLANNING
    path('planning/', planning_views.planning, name='planning'),
    #path('planning/<int:jour_id>/', planning_views.jour, name='jour'),
    path('planning_ajout/', planning_views.ajout_salle, name='ajout_salle'),
    path('planning_update/', planning_views.update_text, name='update_text'),
]
