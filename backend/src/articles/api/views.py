from rest_framework import permissions
#from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework import viewsets
from articles.models import Article
from .serializers import ArticleSerializer

#class ArticleListView(ListAPIView):
    #queryset  = Article.objects.all()
    #serializer_class =  ArticleSerializer

#class ArticleCreateView(CreateAPIView):
    #queryset  = Article.objects.all()
    #serializer_class =  ArticleSerializer
#    permission_classes = (permissions.IsAuthenticated, )

#class ArticleUpdateView(UpdateAPIView):
    #queryset  = Article.objects.all()
    #serializer_class =  ArticleSerializer
    #permission_classes = (permissions.IsAuthenticated, )

#class ArticleDestroyView(DestroyAPIView):
    #queryset  = Article.objects.all()
    #serializer_class =  ArticleSerializer
    #permission_classes = (permissions.IsAuthenticated, )

#class ArticleDetailView(RetrieveAPIView):
    #queryset  = Article.objects.all()
    #serializer_class =  ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()