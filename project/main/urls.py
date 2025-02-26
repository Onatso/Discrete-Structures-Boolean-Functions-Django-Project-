from django.urls import path
# Импортируем созданное нами представление
from .views import TaskList,TaskDetail


urlpatterns = [
   path('', TaskList.as_view(),name = 'task_list'),

   path('<int:pk>', TaskDetail.as_view(),name = 'task_detail')
]