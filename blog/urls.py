from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv', views.cv, name='cv'),
    path('cv/new_coding', views.coding_edit, name='new_coding'),
    path('cv/new_academic', views.academic_edit, name='new_academic'),
    path('cv/new_interest', views.interest_edit, name='new_interest'),
    path('cv/new_achievement', views.achievement_edit, name='new_achievement'),

]
