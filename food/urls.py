from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name="index"),

    path('<int:pk>/',views.FoodDetails.as_view(), name="detail"),

    path('item/', views.item, name='item'),
    # add
    path('add/', views.CreateItem.as_view(), name='create_item'),
    # update
    path('update/<int:id>/', views.update_item, name="update_item"),
    # delete Items
    path('delete/<int:id>/',views.delete_item, name="delete_item"),

]
