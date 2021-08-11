from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/', include('Surveys.urls')),
    path('accounts/', include('Accounts.urls')),
    path('',views.landingPage, name = "landingPage"),
    path('home/',views.home, name="list")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)