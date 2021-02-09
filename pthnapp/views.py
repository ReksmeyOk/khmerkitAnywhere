# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404


from .models import PTHN_Chapter, PTHN_Unit
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count


def get_pthn_chapter_count():
    queryset = PTHN_Unit\
        .objects\
        .values('chapter__title')\
        .annotate(Count('chapter__title'))
    return queryset

def pthn_chapter_list(request):
    unit_list = PTHN_Unit.objects.all().order_by('-id')
    context = {
        'queryset': unit_list,
    }
    return render(request, "pthn_chapter_list.html", context)

def pthn_each_chapter(request, pthncpt):
    chapter_units = PTHN_Unit.objects.filter(chapter=pthncpt)
    query = request.GET.get('q')
    if query:
        chapter_units = chapter_units.filter(Q(mathcpt__icontains=query)
        )
    context = {
        'pthncpt' : pthncpt,
        'chapter_units': chapter_units
    }
    return render(request, 'pthn_each_chapter.html', context)

class PTHNView(ListView):
    model = PTHN_Unit
    chapter_count = get_pthn_chapter_count()
    #print(unit_count)

    def get(self, request, *args, **kwargs):
        context = {
            'units': PTHN_Unit.objects.all().order_by('-id'),
            'chapter_count' : get_pthn_chapter_count
        }
        return render(request, "pthn.html", context)

class PTHNDetailView(DetailView):
    model = PTHN_Unit
    template_name = "pthn_details.html"

    def get_context_data(self, **kwargs):
        context = super(PTHNDetailView, self).get_context_data(**kwargs)
        return context

def pthn_search (request):
    queryset = PTHN_Unit.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'pthn_search_result.html', context)

