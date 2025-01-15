
from django.contrib import admin
from django.urls import path
from app_expert import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('expertEmCifras/', views.expertEmCifras, name='expertEmCifras'),
    path('enviar_email/', views.enviar_email, name='enviar_email'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
