from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from .models import Post, Comment, Favorite, UserProfile
from django.contrib import messages
from .forms import CommentForm, PostForm, ProfilePictureForm, CustomUserChangeForm
from geopy.distance import geodesic


class PostList(generic.ListView):
    """
    Display a list of blog posts with pagination.

    Inherits:
        generic.ListView: The base class for creating list views.

    Attributes:
        model (Model): The model to query for the list view.
        template_name (str): The template to render for the view.
        paginate_by (int): The number of items to display per page.
    """

    model = Post
    template_name = "discover/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """Add context data for the template."""
        context = super().get_context_data(**kwargs)
        context["google_maps_api_key"] = settings.GOOGLE_MAPS_API_KEY
        context["google_maps_map_id"] = settings.GOOGLE_MAPS_MAP_ID
        context["title"] = self.request.GET.get("title", "")
        context["location"] = self.request.GET.get("location", "")
        context["latitude"] = self.request.GET.get("latitude", "")
        context["longitude"] = self.request.GET.get("longitude", "")
        if self.request.user.is_authenticated:
            context["favorites"] = Favorite.objects.filter(user=self.request.user)
            context["comments"] = Comment.objects.filter(author=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        """Handle GET requests, including AJAX requests for pagination."""
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            page = request.GET.get("page")
            posts = Post.objects.all()
            paginator = Paginator(posts, self.paginate_by)
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = []
            post_html = render_to_string(
                "discover/post_list_partial.html",
                {"object_list": posts},
                request=request,
            )
            return JsonResponse({"posts": post_html, "has_next": posts.has_next()})
        else:
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Filter the queryset based on title, location, and proximity to the user's location."""
        queryset = Post.objects.filter(status=1)
        title = self.request.GET.get("title")
        location = self.request.GET.get("location")
        latitude = self.request.GET.get("latitude")
        longitude = self.request.GET.get("longitude")
        min_budget = self.request.GET.get("min_budget")
        max_budget = self.request.GET.get("max_budget")

        if title:
            queryset = queryset.filter(title__icontains=title)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if latitude and longitude:
            user_location = (float(latitude), float(longitude))
            radius = 50  # Radius in kilometers
            posts_within_radius = []
            for post in queryset:
                post_location = (post.latitude, post.longitude)
                distance = geodesic(user_location, post_location).km
                if distance <= radius:
                    posts_within_radius.append(post.id)
            queryset = queryset.filter(id__in=posts_within_radius)
        if min_budget:
            queryset = queryset.filter(budget__gte=min_budget)
        if max_budget:
            queryset = queryset.filter(budget__lte=max_budget)

        return queryset


def post_detail(request, slug):
    """
    Display an individual :model:`discover.Post`.

    **Context**

    ``post``
        An instance of :model:`discover.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted successfully."
            )

    return render(
        request,
        "discover/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Edit an existing comment.

    **Context**

    ``comment_form``: Form for editing a comment.

    **Template:**

    :template:`discover/post_detail.html`
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an existing comment.

    **Context**

    ``comment``: The comment to be deleted.

    **Template:**

    :template:`discover/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def add_favorite(request, slug):
    """
    Add a post to the user's favorites.

    **Context**

    ``post``: The post to be added to favorites.

    **Template:**

    :template:`discover/post_detail.html`
    """
    post = get_object_or_404(Post, slug=slug)
    favorite, created = Favorite.objects.get_or_create(user=request.user, post=post)
    if created:
        messages.success(request, "Added to favorites")
    else:
        messages.info(request, "Already in favorites")
    return redirect("post_detail", slug=slug)


def remove_favorite(request, slug):
    """
    Remove a post from the user's favorites.

    **Context**

    ``post``: The post to be removed from favorites.

    **Template:**

    :template:`discover/post_detail.html`
    """
    post = get_object_or_404(Post, slug=slug)
    favorite = Favorite.objects.filter(user=request.user, post=post)
    if favorite.exists():
        favorite.delete()
        messages.success(request, "Removed from favorites")
    else:
        messages.info(request, "Not in favorites")
    return redirect("post_detail", slug=slug)


def user_profile(request):
    """
    Display the user's profile with options to update profile picture.

    **Context**

    ``user``: The currently logged-in user.
    ``comments``: List of comments made by the user.
    ``favorites``: List of posts favorited by the user.
    ``form``: Form for updating profile picture.

    **Template:**

    :template:`discover/user_profile.html`
    """
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile picture updated successfully!")
            return redirect("user_profile")
    else:
        form = ProfilePictureForm(instance=profile)

    comments = Comment.objects.filter(author=user).order_by("-created_on")
    favorites = Favorite.objects.filter(user=user).order_by("-created_on")
    return render(
        request,
        "discover/user_profile.html",
        {"user": user, "comments": comments, "favorites": favorites, "form": form},
    )


def add_post(request):
    """
    Add a new blog post.

    **Context**

    ``form``: Form for adding a new post.

    **Template:**

    :template:`discover/add_post.html`
    """
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to add a post.")
        return redirect("home")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.save()
            messages.success(request, "Post added successfully!")
            return redirect("home")
    else:
        form = PostForm()

    return render(request, "discover/add_post.html", {"form": form})


def update_user_info(request):
    user = request.user
    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile was updated successfully!")
            return redirect("user_profile")
    else:
        user_form = CustomUserChangeForm(instance=user)
    return render(request, "discover/update_user_info.html", {"user_form": user_form})
