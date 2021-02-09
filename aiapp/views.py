# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404


from .models import AI_Chapter, AI_Unit
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count


def get_ai_chapter_count():
    queryset = AI_Unit\
        .objects\
        .values('chapter__title')\
        .annotate(Count('chapter__title'))
    return queryset

def ai_chapter_list(request):
    unit_list = AI_Unit.objects.all().order_by('-id')
    context = {
        'queryset': unit_list,
    }
    return render(request, "ai_chapter_list.html", context)

def ai_each_chapter(request, aicpt):
    chapter_units = AI_Unit.objects.filter(chapter=aicpt)
    query = request.GET.get('q')
    if query:
        chapter_units = chapter_units.filter(Q(cpt__icontains=query)
        )
    context = {
        'aicpt' : aicpt,
        'chapter_units': chapter_units
    }
    return render(request, 'ai_each_chapter.html', context)

class AIView(ListView):
    model = AI_Unit
    chapter_count = get_ai_chapter_count()
    #print(unit_count)

    def get(self, request, *args, **kwargs):
        context = {
            'units': AI_Unit.objects.all().order_by('-id'),
            'chapter_count' : get_ai_chapter_count
        }
        return render(request, "ai.html", context)

class AIDetailView(DetailView):
    model = AI_Unit
    template_name = "ai_details.html"

    def get_context_data(self, **kwargs):
        context = super(AIDetailView, self).get_context_data(**kwargs)
        return context

def ai_search (request):
    queryset = AI_Unit.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'ai_search_result.html', context)

