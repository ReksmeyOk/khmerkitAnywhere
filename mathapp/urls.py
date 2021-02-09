from django.urls import path
from . import views
from .views import MATHView, MATHDetailView

from newsapp.views import IndexView
from aiapp.views import AIView
from englishapp.views import ENGView
from pthnapp.views import PTHNView

urlpatterns = [
    path('', IndexView.as_view(), name= "news-page"),
    # path('news/<int:pk>/', ArticleDetailView.as_view(), name = "news-details"),
    # path('search/', views.search, name = 'search-result-page'),

    path('mathematics_tutorial/', MATHView.as_view(), name='math-page'),
    path('mathematics_tutorial/<int:pk>/', MATHDetailView.as_view(), name="math-details"),
    path('mathematics_search/', views.math_search, name = 'math-search-result-page'),
    path('mathematics_chapter_list/', views.math_chapter_list, name='math-chapter-list-page'),
    path('mathematics_chapter/<str:mathcpt>/', views.math_each_chapter, name='math-each-chapter-page'),

    path('artificial_intelligence_tutorial/', AIView.as_view(), name='ai-page'),
    path('english_tutorial/', ENGView.as_view(), name='eng-course-page'),
    path('python_tutorial/', PTHNView.as_view(), name='python-page')
]
#Note:  For all the functions views.index, views.englishcourse, views.mathematics
#       views.artificialintelligence, and views.post, their () are dropped
#       when we dont need their default values
