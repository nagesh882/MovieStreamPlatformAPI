from django.urls import path
from imdb_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.api_root, name="entry-points-api"),

    path('list/', views.movie_list, name='movie-list'),

    path('list/<int:pk>', views.movie_detail, name='movie-details'),

    path('stream/', views.stream_list, name='stream-platform'),

    path('stream/<int:pk>', views.stream_detail, name='stream-platform-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)