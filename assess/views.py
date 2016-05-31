from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Rating, Criteria, Marks


def index(request):
    ratings_list = Rating.objects.all()
    context = {'ratings_list':ratings_list}
    return render(request, 'assess/index.html', context)


def detail(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    return render(request, 'assess/detail.html', {'rating':rating})

