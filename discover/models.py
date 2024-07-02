from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

CURRENCY_CHOICES = (
    ('EUR', 'Euro'),
    ('CHF', 'Swiss Franc'),
    ('GBP', 'Pound Sterling')
)


class Post(models.Model):
    """
    Represents a blog post in the application.

    Attributes:
        title (str): The title of the post.
        slug (str): URL-friendly identifier for the post.
        author (User): The author of the post.
        featured_image (CloudinaryField): The featured image for the post.
        content (str): The full content of the post.
        created_on (datetime): Timestamp when the post was created.
        updated_on (datetime): Timestamp when the post was last updated.
        status (int): The status of the post (draft or published).
        excerpt (str): A short description or summary of the post.
        budget (Decimal): The budget for the place.
        currency (str): The currency of the budget.
        location (str): The location of the place.
        latitude (Decimal): Latitude for the map.
        longitude (Decimal): Longitude for the map.
        nights (int): Number of nights (optional).
        people (int): Number of people (optional).
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField(
        'image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    budget = models.DecimalField(
        max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6)
    nights = models.IntegerField(blank=True, null=True)
    people = models.IntegerField(blank=True, null=True)

    class Meta:
        # Default ordering of posts (most recent first)
        ordering = ['-created_on']

    def __str__(self):
        return self.title  # String representation of the post


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (Post): The post that the comment is associated with.
        author (User): The author of the comment.
        body (str): The content of the comment.
        created_on (datetime): Timestamp when the comment was created.
        approved (bool): Whether the comment is approved or not.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Favorite(models.Model):
    """
    Represents a favorite post for a user.

    Attributes:
        post (Post): The post that is marked as favorite.
        user (User): The user who marked the post as favorite.
        created_on (datetime): Timestamp when the favorite was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="favorites")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorites")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')
        ordering = ['-created_on']

    def __str__(self):
        return f"Favorite {self.post} by {self.user}"


class UserProfile(models.Model):
    """
    Represents a user's profile.

    Attributes:
        user (User): The user associated with the profile.
        profile_picture (CloudinaryField): The profile picture of the user.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
