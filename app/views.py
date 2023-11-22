from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

job_title = ["First Job", "Second Job"]

job_description = ["First Job Description", "Second Job Description"]


# Create your views here.
def job_list(request):
    """Render the Job List Page.

    :param HTTPRequest request: The HTTP request object
    :return HTTPResponce: The HTTP Responce containing the Job List.
    """
    return_html = f"""<ul>{''.join([f'<li><a href={reverse("job_detail", args=(index,))}>{job}</a></li>' for index, job in enumerate(job_title)])}</ul>"""
    return HttpResponse(return_html)


def job_detail(request, id):
    """Render the Job Detail Page.
    <domain>/job/<int:id>

    This view displays detailed information about a job based on the provided job ID.

    :param HTTPRequest request: The HTTP request object.
    :param int id: Job ID number
    :return HTTPResponce: The HTTP response containing the job details page.
    :raise Http404: Job ID does not exisit
    """
    if id == 0:
        # Redirects to the home page if the ID is 0.
        return redirect(reverse("job_home"))

    try:
        job_title_text, job_description_text = job_title[id], job_description[id]
    except IndexError:
        raise HttpResponseNotFound("Job not found.")

    # Builds the HTML content for the details page.
    return_html = f"<h1>{job_title_text}</h1> <h3>{job_description_text}</h3>"
    return HttpResponse(return_html)
