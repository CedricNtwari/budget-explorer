from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page.

    This view function fetches the most recently updated About instance from the About model
    and renders the 'about/about.html' template with this instance.

    **Context:**
    - `about`: An instance of the About model representing the latest updated information.

    **Template:**
    - `about/about.html`: The template rendered to display the About page.

    Args:
    - `request`: The HttpRequest object representing the current request.

    Returns:
    - `HttpResponse`: The rendered template with the context data.
    """
    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
