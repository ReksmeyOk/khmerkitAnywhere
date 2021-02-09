from django.urls import path
from . import views
from .views import AIView, AIDetailView

from englishapp.views import ENGView
from mathapp.views import MATHView
from newsapp.views import IndexView
from pthnapp.views import PTHNView

urlpatterns = [
    path('', IndexView.as_view(), name= "news-page"),
    # path('news/<int:pk>/', ArticleDetailView.as_view(), name = "news-details"),
    # path('search/', views.search, name = 'search-result-page'),

    path('artificial_intelligence_tutorial/', AIView.as_view(), name='ai-page'),
    path('ai_tutorial/<int:pk>/', AIDetailView.as_view(), name="ai-details"),
    path('ai_search/', views.ai_search, name = 'ai-search-result-page'),
    path('ai_chapter_list/', views.ai_chapter_list, name='ai-chapter-list-page'),
    path('ai_chapter/<str:aicpt>/', views.ai_each_chapter, name='ai-each-chapter-page'),

    path('english_tutorial/', ENGView.as_view(), name='eng-course-page'),
    path('mathematics_tutorial/', MATHView.as_view(), name='math-page'),
    path('python_tutorial/', PTHNView.as_view(), name='python-page'),
]
#Note:  For all the functions views.index, views.englishcourse, views.mathematics
#       views.artificialintelligence, and views.post, their () are dropped
#       when we dont need their default values
