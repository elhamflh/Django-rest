from rest_framework.generics import(ListCreateAPIView,RetrieveUpdateDestroyAPIView) 
from .serializers import ArticleSerializer , UserSerializer
from blog.models import Article
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser                                
from .permissions import (IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperuserOrStaffReadOnly)
# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes =(IsStaffOrReadOnly,IsAuthorOrReadOnly)
    
   
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializer
    permission_classes = (IsSuperUser,IsSuperuserOrStaffReadOnly)
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,IsSuperuserOrStaffReadOnly)   
    # lookup_field = 'pk'  
    # میتونیم بهش اسلاگ رو بدیم.
    # و باید از یوارال هم اسلاگ 
    # بدیم