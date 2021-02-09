from django.shortcuts import render

# Create your views here.
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404


from .models import Math_Chapter, Math_Unit
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count


def get_math_chapter_count():
    queryset = Math_Unit\
        .objects\
        .values('chapter__title')\
        .annotate(Count('chapter__title'))
    return queryset

def math_chapter_list(request):
    unit_list = Math_Unit.objects.all().order_by('-id')
    context = {
        'queryset': unit_list,
    }
    return render(request, "math_chapter_list.html", context)

def math_each_chapter(request, mathcpt):
    chapter_units = Math_Unit.objects.filter(chapter=mathcpt)
    query = request.GET.get('q')
    if query:
        chapter_units = chapter_units.filter(Q(mathcpt__icontains=query)
        )
    context = {
        'mathcpt' : mathcpt,
        'chapter_units': chapter_units
    }
    return render(request, 'math_each_chapter.html', context)

class MATHView(ListView):
    model = Math_Unit
    chapter_count = get_math_chapter_count()
    #print(unit_count)

    def get(self, request, *args, **kwargs):
        context = {
            'units': Math_Unit.objects.all().order_by('-id'),
            'chapter_count' : get_math_chapter_count
        }
        return render(request, "math.html", context)

class MATHDetailView(DetailView):
    model = Math_Unit
    template_name = "math_details.html"

    def get_context_data(self, **kwargs):
        context = super(MATHDetailView, self).get_context_data(**kwargs)
        return context

def math_search (request):
    queryset = Math_Unit.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )
    context = {
        'queryset' : queryset
    }
    return render(request, 'math_search_result.html', context)

