from django.shortcuts import render

# Create your views here.
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404


from .models import English_Chapter, English_Unit
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count


def get_eng_chapter_count():
    queryset = English_Unit\
        .objects\
        .values('chapter__title')\
        .annotate(Count('chapter__title'))
    return queryset

def eng_chapter_list(request):
    unit_list = English_Unit.objects.all().order_by('-id')
    context = {
        'queryset': unit_list,
    }
    return render(request, "english_chapter_list.html", context)

def eng_each_chapter(request, engcpt):
    chapter_units = English_Unit.objects.filter(chapter=engcpt)
    query = request.GET.get('q')
    if query:
        chapter_units = chapter_units.filter(Q(cpt__icontains=query)
        )
    context = {
        'engcpt' : engcpt,
        'chapter_units': chapter_units
    }
    return render(request, 'english_each_chapter.html', context)

class ENGView(ListView):
    model = English_Unit
    chapter_count = get_eng_chapter_count()
    #print(unit_count)

    def get(self, request, *args, **kwargs):
        context = {
            'units': English_Unit.objects.all().order_by('-id'),
            'chapter_count' : get_eng_chapter_count
        }
        return render(request, "english.html", context)

class ENGDetailView(DetailView):
    model = English_Unit
    template_name = "english_details.html"

    def get_context_data(self, **kwargs):
        context = super(ENGDetailView, self).get_context_data(**kwargs)
        return context

def eng_search (request):
    queryset = English_Unit.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'english_search_result.html', context)

