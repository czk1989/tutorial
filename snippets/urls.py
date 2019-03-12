from django.urls import path,include
from snippets import views,views_cls
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     path('', views.api_root),
#     path('snippets/', views_cls.SnippetList.as_view(),name='snippet-list'),
#     path('snippets/<int:pk>/', views_cls.SnippetDetail.as_view(),name='snippet-detail'),
#     path('users/', views_cls.UserList.as_view(),name='user-list'),
#     path('users/<int:pk>/', views_cls.UserDetail.as_view(),name='user-detail'),
#     path('snippets/<int:pk>/highlight/', views_cls.SnippetHighlight.as_view(),name='snippet-highlight'),
# ]
#
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
#


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from snippets.views_cls import SnippetViewSet, UserViewSet
from snippets.views import api_root
from rest_framework import renderers
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')
# Create a router and register our viewsets with it.

#
#
#
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

router = DefaultRouter()
router.register(r'snippets', views_cls.SnippetViewSet)
router.register(r'users', views_cls.UserViewSet)


# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#     # path('', include(router.urls)),
# ])


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]

