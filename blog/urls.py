from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv', views.cv, name='cv'),
    path('cv/new_coding', views.coding_new, name='new_coding'),
    path('cv/new_academic', views.academic_new, name='new_academic'),
    path('cv/new_interest', views.interest_new, name='new_interest'),
    path('cv/new_achievement', views.achievement_new, name='new_achievement'),
    path('coding/<int:pk>/edit/', views.coding_edit, name='coding_edit'),
    path('academic/<int:pk>/edit/', views.academic_edit, name='academic_edit'),
    path('interest/<int:pk>/edit/', views.interest_edit, name='interest_edit'),
    path('achievement/<int:pk>/edit/', views.achievement_edit, name='achievement_edit'),


]
