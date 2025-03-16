from django.urls import path
from . import views
from . import permissions
from .views import *

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('images/<int:pk>/', views.ImageView.as_view(), name='image-detail'),
    path('permissions/', permissions.WorkingDays, name='permission'),
    path('comment-list/', views.CommentListCreateView.as_view(), name='comment-list-create'),
]