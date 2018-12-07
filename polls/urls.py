from django.urls import path 
from . import views 

#SET APP_NAME TO MAKE THESE URL PATTERNS FALL UNDER ITS NAMESPACE (avoids mistaken url patterns from other apps with the same directory names)
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
