from . import views
from django.urls import path
from .views import add_post, add_favorite, remove_favorite, user_profile

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # Move this before the slug patterns
    path('profile/', user_profile, name='user_profile'),
    path('add_post/', add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/favorite/', add_favorite, name='add_favorite'),
    path('post/<slug:slug>/unfavorite/',
         remove_favorite, name='remove_favorite'),
]
