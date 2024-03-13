
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_us, name='about'),
    path('home_category/<slug:category_slug>/', views.home_Category, name='home_category'),
    path('category/<slug:category_slug>/',views.home, name='category_wise_post'),
    path('admin/', admin.site.urls),
    path('author/', include("author.urls")),
    path('post/', include("post.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)