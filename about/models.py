from django.db import models


class About(models.Model):
    """
    Model representing the 'About' information for the site.

    Attributes:
        title (str): The title of the about section.
        updated_on (datetime): The timestamp when the entry was last updated.
        content (str): The detailed content of the about section.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
