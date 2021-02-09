from django.shortcuts import render

# Create your views here.
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Post
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import Count

# Dummy posts
# posts = [
#     {
#         'author': 'Ousah',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 28, 2020',
#         'author_email': 'okreksmey@gmail.com',
#
#     },
#     {
#         'author': 'Oudom',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 29, 2020',
#         'author_email': 'okreksmey@gmail.com',
#
#     }
# ]
#
# def index(request):
#     context = {
#         'posts': Post.objects.all().order_by('-id')
#     }
#     return render(request, "blogapp/index.html", context)


def get_category_count():
    queryset = Post\
        .objects\
        .values('category__title')\
        .annotate(Count('category__title'))
    return queryset

def category_list(request):
    post_list = Post.objects.all().order_by('-id')
    context = {
        'queryset': post_list,
    }
    return render(request, "category_list.html", context)

def each_category(request, cts):
    category_posts = Post.objects.filter(category=cts)
    query = request.GET.get('q')
    if query:
        category_posts = category_posts.filter(Q(cts__icontains=query)
        )
    context = {
        'cts': cts,
        'category_posts': category_posts
    }
    return render(request, 'each_category.html', context)

class IndexView(ListView):
    model = Post
    category_count = get_category_count()
    #print(category_count)

    def get(self, request, *args, **kwargs):
        context = {
            'posts': Post.objects.all().order_by('-id'),
            'category_count' : get_category_count,
            # 'most_recent': Post.objects.order_by('-timestamp')[:3]
        }
        return render(request, "index.html", context)

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        return context

def search (request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    context = {
        'queryset': queryset
    }
    return render(request, 'search_result.html', context)
#
# class AddCommentView(CreateView):
#     model = Comment
#     form_class = CommentForm
#     template_name = 'article_details.html'
#     # fields = '__all__'
