from django.shortcuts import render


def handler404(request, template_name="404.html"):
    """
    Custom handler for 404 errors (Page Not Found).

    Args:
        request (HttpRequest): The request object used to generate this response.
        exception (Exception): The exception that triggered this 404 error.
        template_name (str): The name of the template to use for rendering the response. Defaults to "404.html".

    Returns:
        HttpResponse: The HTTP response object with status code 404.
    """
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, template_name="500.html"):
    """
    Custom handler for 500 errors (Internal Server Error).

    Args:
        request (HttpRequest): The request object used to generate this response.
        template_name (str): The name of the template to use for rendering the response. Defaults to "500.html".

    Returns:
        HttpResponse: The HTTP response object with status code 500.
    """
    response = render(request, template_name)
    response.status_code = 500
    return response
