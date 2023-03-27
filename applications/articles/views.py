from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters 
from .models import Article, Tag, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, TagSerializer, CommentSerializer
from .permissions import IsAuthor 

class ArticleViewSet(ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['tag', 'status']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tag__title'] 

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context 
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated] 
        elif self.action in ['update', 'delete']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return super().get_serializer_class()


"""
actions - действия пользователя 
list
retrieve
create 
update 
delete
"""

    
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 
    
    
class CommentViewSet(ModelViewSet):
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'destroy']:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context 