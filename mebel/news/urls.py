from django.urls import path
from news.views import HomeNews, NewsByCategory, ViewNews, AddNews


app_name = "news"
urlpatterns = [
    path('', HomeNews.as_view(), name='News'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('<int:pk>', ViewNews.as_view(), name='News'),
    path('add_news/', AddNews.as_view(), name='Add_news'),
]
