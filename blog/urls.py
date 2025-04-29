from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('',views.PostList.as_view()),
    path('about_me/', include('single_pages.urls')),
    path('landing/', include('single_pages.urls')),
    #path('',views.index),
    #path('<int:pk>/', views.single_post_page),
]