from django.shortcuts import render
from django.views import generic
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = 'discover/index.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        context['google_maps_map_id'] = settings.GOOGLE_MAPS_MAP_ID
        return context

    def get(self, request, *args, **kwargs):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            page = request.GET.get('page')
            posts = Post.objects.all()
            paginator = Paginator(posts, self.paginate_by)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = []
            post_html = render_to_string('discover/post_list_partial.html', {'object_list': posts}, request=request)
            return JsonResponse({'posts': post_html, 'has_next': posts.has_next()})
        else:
            return super().get(request, *args, **kwargs)
