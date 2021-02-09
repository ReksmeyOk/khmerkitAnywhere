from django.urls import path
from . import views
from .views import IndexView, ArticleDetailView

from englishapp.views import ENGView
from mathapp.views import MATHView
from aiapp.views import AIView
from pthnapp.views import PTHNView

urlpatterns = [
    path('', IndexView.as_view(), name= "news-page"),
    path('news_detail/<int:pk>/', ArticleDetailView.as_view(), name = "news-details"),
    path('search/', views.search, name = 'search-result-page'),
    path('categorylist/', views.category_list, name='category-list-page'),
    path('category/<str:cts>/', views.each_category, name='each-category-page'),

    path('english_tutorial/', ENGView.as_view(), name='eng-course-page'),
    path('mathematics_tutorial/', MATHView.as_view(), name='math-page'),
    path('artificial_intelligence_tutorial/', AIView.as_view(), name='ai-page'),
    path('python_tutorial/', PTHNView.as_view(), name='python-page'),
]
#Note:  For all the functions views.index, views.englishcourse, views.mathematics
#       views.artificialintelligence, and views.post, their () are dropped
#       when we dont need their default values
