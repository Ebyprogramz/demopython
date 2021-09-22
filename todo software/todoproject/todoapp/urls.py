from django.urls import path
from .import views

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('newpage/',views.view.as_view(),name='newpage'),
    path('lstpage/<int:pk>/', views.newview.as_view(), name='lstpage'),
    path('pageupdate/<int:pk>/', views.updatetask.as_view(), name='pageupdate'),
    path('pagedelete/<int:pk>/', views.deletetask.as_view(),name='pagedelete'),
]