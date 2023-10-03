from django.urls import path
from works.views import WorksPage, WorksByCategory, WorkView

urlpatterns = [
    path('', WorksPage.as_view(), name='works'),
    path('category/<int:pk>', WorksByCategory.as_view(), name='by_category'),
    path('work/<int:pk>', WorkView.as_view(), name="work_view")    
]
