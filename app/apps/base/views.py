from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template

def home(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, "auth/login.html")


def crm_dashboard(request):
    return render(request, "crm/dashboard.html")


def superadmin_dashboard(request):
    return render(request, "superadmin/dashboard.html")


def section_page(request, section, page):
    if ".." in page or page.startswith("/"):
        raise Http404("Invalid path")

    template_name = f"{section}/{page}"

    try:
        get_template(template_name)
    except Exception as exc:
        raise Http404("Page not found") from exc

    return render(request, template_name)