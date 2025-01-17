from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, BMICalculatorView, BMIRecordListView, BMIRecordDetailView, BMIRecordUpdateView, BMIRecordDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'), 
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('bmi_calculator/', BMICalculatorView.as_view(), name='bmi_calculator'),
    path('bmi_records/', BMIRecordListView.as_view(), name='bmi_record_list'),
    path('bmi_records/<int:pk>/', BMIRecordDetailView.as_view(), name='bmi_detail'),
    path('bmi_records/<int:pk>/edit/', BMIRecordUpdateView.as_view(), name='bmi_update'),
    path('bmi_records/<int:pk>/delete/', BMIRecordDeleteView.as_view(), name='bmi_delete'),
]