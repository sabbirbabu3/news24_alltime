from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.CreatePostView.as_view(), name='post'),
    path('details/<int:id>/', views.UserDetailView.as_view(), name='details' ),
    path('edit/<int:id>/', views.EditpostView.as_view(), name='edit' ),
    # path('delete/<int:id>/', views.deleteView, name='delete' ),
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete' ),

]
