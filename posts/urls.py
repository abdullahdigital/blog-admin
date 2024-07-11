from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
     path('post/<str:pk>/', views.post, name='post_detail'),
    path('chart-data/', views.chart_data, name='chart_data'),
    path('blog/', views.blog_list, name='blog_list'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_submission, name='contact'),
     path('subscribe/', views.subscribe, name='subscribe'),
    #path('contact-chart/', views.contact_chart, name='contact_chart'),
    #path('author-chart/', views.author_chart, name='author_chart'),
]