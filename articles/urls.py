from django.urls import path
from .views import articles_by_year_month, articles_by_year, article_2023

urlpatterns = [
    path('', articles_by_year_month, name='articles_by_year_month'),
    path('2023/', article_2023, name='article_2023'),
    path('<int:year>/', articles_by_year, name='articles_by_year'),
    path('<int:year>/<int:month>/', articles_by_year_month, name='articles_by_year_month'),
]
