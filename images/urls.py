from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:pk>/<slug:slug>/', views.image_detail, name='detail'),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
