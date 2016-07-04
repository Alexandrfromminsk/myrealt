from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MarkForm


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
    criterias = Criteria.get_ordered_list(Criteria) #Criteria.objects.all()
    return render(request, 'assess/full_index.html', {'ratings':ratings, 'criterias':criterias})

def add_form(request):
    if request.method == "POST":
        myform = MarkForm(request.POST)
        if myform.is_valid:
            new_marks = myform.save(commit=False)
            #new_marks.save()
            return redirect('full_index')
    else:
        myform = MarkForm()
    return render(request, 'assess/add_form.html', {'form':myform})