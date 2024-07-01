from . import views
from django.urls import path
from .views import add_favorite, remove_favorite

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/favorite/', add_favorite, name='add_favorite'),
    path('post/<slug:slug>/unfavorite/',
         remove_favorite, name='remove_favorite'),
]
