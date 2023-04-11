from django.contrib import admin
from django.urls import path
from main_site import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view(), name='index'),
    path('original_builds/', views.OriginalBuildsView.as_view(), name='original_builds'),
    path('character_detail/<int:pk>/', views.PersonagemOriginalDetailView.as_view(), name='character_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)