from django.urls import path
from orders import views

urlpatterns = [
  path('', views.client_list, name='index'),
  path('clients/', views.client_list, name='client_list'),
  path('clients/create/', views.client_create, name='client_create'),
  path('clients/edit/<int:id>/', views.client_edit, name='client_edit'),
  path('clients/delete/<int:id>/', views.client_delete, name='client_delete'),
  
  path('dishes/', views.dish_list, name='dish_list'),
  path('dishes/create/', views.dish_create, name='dish_create'),
  path('dishes/edit/<int:id>/', views.dish_edit, name='dish_edit'),
  path('dishes/delete/<int:id>/', views.dish_delete, name='dish_delete'),
  
  path('tables/', views.table_list, name='table_list'),
  path('tables/create/', views.table_create, name='table_create'),
  path('tables/edit/<int:id>/', views.table_edit, name='table_edit'),
  path('tables/delete/<int:id>/', views.table_delete, name='table_delete'),
  
  path('waiters/', views.waiter_list, name='waiter_list'),
  path('waiters/create/', views.waiter_create, name='waiter_create'),
  path('waiters/edit/<int:id>/', views.waiter_edit, name='waiter_edit'),
  path('waiters/delete/<int:id>/', views.waiter_delete, name='waiter_delete'),
  
  path('orders/', views.order_list, name='order_list'),
  path('orders/create/', views.order_create, name='order_create'),
  path('orders/edit/<int:id>/', views.order_edit, name='order_edit'),
  path('orders/delete/<int:id>/', views.order_delete, name='order_delete'),
  
  path('payments/', views.payment_list, name='payment_list'),
  path('payments/create/', views.payment_create, name='payment_create'),
  path('payments/edit/<int:id>/', views.payment_edit, name='payment_edit'),
  path('payments/delete/<int:id>/', views.payment_delete, name='payment_delete'),
]