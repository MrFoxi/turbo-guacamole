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
from django.urls import path
from preview_app import views as preview_app_views
from conference import views as conference_views
from planning import views as planning_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # CONFERENCE
    path('conference/', conference_views.index, name='conference'),

    # PLANNING
    path('planning/', planning_views.planning, name='planning'),
    #path('planning/<int:jour_id>/', planning_views.jour, name='jour'),

    # path('hello/', views.hello)
]
