from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MarkForm


from .models import Rating, Criteria, Marks
import operator

def index(request):
    ratings_list = Rating.objects.all()
    for item in ratings_list:
        item.calc_rating

    ordered = sorted(ratings_list, key=operator.attrgetter('rating'), reverse=True)[:10]
    context = {'ratings_list': ordered}
    return render(request, 'assess/index.html', context)


def detail(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    criterias = Criteria.get_ordered_list(Criteria)
    return render(request, 'assess/detail.html', {'rating':rating, 'criterias':criterias})

def full_index(request):
    ratings = Rating.objects.all()
    criterias = Criteria.get_ordered_list(Criteria) #Criteria.objects.all()
    return render(request, 'assess/full_index.html', {'ratings':ratings, 'criterias':criterias})

def add_form(request):
    criteria = Criteria.get_ordered_list(Criteria)
    if request.method == 'POST':
        myform = MarkForm(Criteria.objects.values_list('name', flat=True),request.POST)
        if myform.is_valid():
            new_flat = Rating()
            new_flat.pseudonim = myform.cleaned_data.get('name_field')
            new_flat.link = myform.cleaned_data.get('link_field')
            new_flat.rating = 0
            new_flat.is_ready=False
            new_flat.save()


            for crit in criteria:
                mark = myform.cleaned_data.get(crit.name)
                new_mark = Marks(pseudonim=new_flat, weight = crit, value=mark)
                new_mark.save()

            return redirect('full_index')

    else:
        myform = MarkForm(Criteria.objects.values_list('name', flat=True))
    return render(request, 'assess/add_form.html', {'form':myform, 'criteria':criteria})

def criteria(request):
    criteria = Criteria.get_ordered_list(Criteria)  # Criteria.objects.all()
    return render(request, 'assess/criteria.html', {'criteria': criteria})
