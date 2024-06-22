from django.shortcuts import render
from django.views import generic
from django.conf import settings
from .models import Post, Comment, Favorite

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'discover/discover_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        context['google_maps_map_id'] = settings.GOOGLE_MAPS_MAP_ID
        return context