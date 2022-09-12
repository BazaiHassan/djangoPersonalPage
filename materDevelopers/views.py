from multiprocessing import context
from django.shortcuts import render
from myGithubApp.models import GithubItem
from myPortfolioApp.models import Portfolio

def index(request):
    githubItems = GithubItem.objects.all().filter(is_available=True)
    portfolioItems = Portfolio.objects.all().filter(is_available=True)

    context = {
        'githubItems':githubItems,
        'portfolioItems':portfolioItems,
    }
    return render(request, 'index.html', context)