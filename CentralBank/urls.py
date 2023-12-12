from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name = "home"),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^profile/', include("profiles.urls")),
    url(r'^admins/', include("admins.urls")),
    url(r'^about/', include("about.urls")),
    url(r'^app/', include("app.urls")),
    url(r'^converter/', include("converter.urls")),
    url(r'^contact/', include("contact.urls")),
    url(r'^pages/', include("pages.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Change Site Title, Index Title and Site Title
admin.site.site_header = "Central Bank Administration"
admin.site.site_title = "Central Bank Administration"
admin.site.index_title = "Welcome to Central Bank Administration Admin Panel"
