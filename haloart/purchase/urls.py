from django.urls import path

from . import views


urlpatterns = [
    path("", views.MainTitleView.as_view(), name="main_page"),
    path("new_product/", views.AddNewProductView.as_view(),
         name="new_product"),
    path('edit_product/<int:pk>/', views.UpdateProductView.as_view(),
         name="edit_product"),
    path('delete_product/<int:pk>/', views.DeleteProductView.as_view(),
         name="delete_product")
]


