from django.urls import path
from . import views

urlpatterns = [
    # untuk post
    path('', views.list_posts, name='blog-home'),
    path('create/', views.create_post, name='create_post'),
    path('list/', views.list_posts, name='list_posts'),
    path('<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('<int:pk>/update/', views.update_post, name='update_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    # untuk kategori
    path('kategori/', views.list_kategori, name='list_kategori'),
    path('create_kategori/', views.create_kategori, name='create_kategori'),
    path('<int:pk>/detail-kategori/', views.kategori_detail, name='kategori_detail'),  
    path('<int:pk>/update-kategori/', views.update_kategori, name='update_kategori'),
    path('<int:pk>/delete-kategori/', views.delete_kategori, name='delete_kategori'),
    # comment
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]