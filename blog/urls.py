from django.urls import path
from .views import ArticleList , Articledetail

app_name='blog'

urlpatterns = [
  path('', ArticleList.as_view(), name='list' ),
  path('<int:pk>',Articledetail.as_view(), name='detail' ),

]

