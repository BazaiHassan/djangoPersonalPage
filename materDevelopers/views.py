from multiprocessing import context
from django.shortcuts import render

from myGithubApp.models import GithubItem

def index(request):
    githubItems = GithubItem.objects.all().filter(is_available=True)

    context = {
        'githubItems':githubItems,
    }
    return render(request, 'index.html', context)