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
    title = models.CharField(max_length=200, unique=True)  # Title of the post
    # URL-friendly identifier
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")  # Author of the post
    featured_image = CloudinaryField(
        'image', default='placeholder')  # Backup image for the post
    content = models.TextField()  # Full content of the post
    # Timestamp when the post was created
    created_on = models.DateTimeField(auto_now_add=True)
    # Timestamp when the post was last updated
    updated_on = models.DateTimeField(auto_now=True)
    # Status of the post (e.g., draft, published)
    status = models.IntegerField(choices=STATUS, default=0)
    # Short description or summary of the post
    excerpt = models.TextField(blank=True)
    budget = models.DecimalField(
        max_digits=10, decimal_places=2)  # Budget for the place
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default='EUR')  # Currency of the budget
    location = models.CharField(max_length=255)  # Location of the place
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6)  # Latitude for the map
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6)  # Longitude for the map
    # Number of nights (optional)
    nights = models.IntegerField(blank=True, null=True)
    # Number of people (optional)
    people = models.IntegerField(blank=True, null=True)

    class Meta:
        # Default ordering of posts (most recent first)
        ordering = ['-created_on']

    def __str__(self):
        return self.title  # String representation of the post


class Comment(models.Model):
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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
