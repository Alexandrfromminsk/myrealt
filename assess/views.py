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

def full_index(request):
    ratings = Rating.objects.all()
    criterias = Criteria.objects.all()
    marks = Marks.objects.all()
    full_ind = {}

    for flat in ratings:
        full_ind[flat] = {}
        flat_marks = Marks.objects.filter(pseudonim=flat)
        for record in flat_marks:
            full_ind[flat][record.weight] = record.value


    return render(request, 'assess/full_index.html', {'ratings':ratings, 'criterias':criterias, 'marks':marks, 'full_index_dict':full_ind})