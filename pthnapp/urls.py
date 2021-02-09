from django.urls import path
from . import views
from .views import PTHNView, PTHNDetailView

from newsapp.views import IndexView, ArticleDetailView
from aiapp.views import AIView, AIDetailView
from englishapp.views import ENGView, ENGDetailView
from mathapp.views import MATHView, MATHDetailView
# from pythonapp.views import PYTHONView, PYTHONDetailView

urlpatterns = [
    path('', IndexView.as_view(), name= "news-page"),
    # path('news/<int:pk>/', ArticleDetailView.as_view(), name = "news-details"),
    # path('search/', views.search, name = 'search-result-page'),

    path('python_tutorial/', PTHNView.as_view(), name='python-page'),
    path('python_tutorial/<int:pk>/', PTHNDetailView.as_view(), name="python-details"),
    path('python_search/', views.pthn_search, name = 'python-search-result-page'),
    path('python_chapter_list/', views.pthn_chapter_list, name='python-chapter-list-page'),
    path('python_chapter/<str:pthncpt>/', views.pthn_each_chapter, name='python-each-chapter-page'),

    path('artificial_intelligence_tutorial/', AIView.as_view(), name='ai-page'),
    path('english_tutorial/', ENGView.as_view(), name='eng-course-page'),
    path('mathematics_tutorial/', MATHView.as_view(), name='math-course-page'),

]
#Note:  For all the functions views.index, views.englishcourse, views.mathematics
#       views.artificialintelligence, and views.post, their () are dropped
#       when we dont need their default values
