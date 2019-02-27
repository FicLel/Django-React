
# from django.urls import path
from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter
# from .views import (ArticleListView,ArticleCreateView, ArticleDetailView,ArticleDestroyView,ArticleUpdateView)
router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
# 		path('<pk>', ArticleDetailView.as_view()),
# 		path('<pk>/update/', ArticleUpdateView.as_view()),
# 		path('<pk>/delete/', ArticleDestroyView.as_view()),
# 	]


