from django.urls import path, re_path
from groups import views 

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroups.as_view(), name='create'),
    re_path(r'posts/in/(?P<slug>[-\w]+/$)', views.SingleGroups.as_view(), name='single')
]