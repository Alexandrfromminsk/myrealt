from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import MarkForm


from .models import Rating, Criteria, Marks


def index(request):
    ratings_list = Rating.objects.all().order_by('rating')
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
    if request.method == 'POST':
        myform = MarkForm(Criteria.objects.values_list('name', flat=True),request.POST)
        if myform.is_valid():
            new_flat = Rating()
            new_flat.pseudonim = myform.cleaned_data.get('name_field')
            new_flat.link = myform.cleaned_data.get('link_field')
            new_flat.rating = 0
            new_flat.is_ready=False
            new_flat.save()
            # try:
            criterias = Criteria.get_ordered_list(Criteria)
            for criteria in criterias:
                mark = myform.cleaned_data.get(criteria.name)
                new_mark = Marks(pseudonim=new_flat, weight = criteria, value=mark)
                new_mark.save()
            #
            # except:
            #     return HttpResponse("Model Errors: %s" % myform.errors.as_json())
            return redirect('full_index')
        # else:
        #     return HttpResponse("Form is not valid: %s" % myform.errors.as_json())
    else:
        myform = MarkForm(Criteria.objects.values_list('name', flat=True))
    return render(request, 'assess/add_form.html', {'form':myform})