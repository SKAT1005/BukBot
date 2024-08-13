from django.shortcuts import render

from app.models import Site


def main_menu(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'main.html', context)
